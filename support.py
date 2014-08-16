import binascii

def chunk(seq, size):
    return [ seq[x:x+size] for x in range(0, len(seq), size) ]

def hexit2ascii(hexit):
    return chr(int(hexit, 16))

def hex2ascii(hex_string):
    return ''.join([ hexit2ascii(hexit) for hexit in chunk(hex_string, 2) ])

def ints2hexit(hex16, hex1):
    return chr(hex16) + chr(hex1)

# only works on hex encoded ascii (even number length, each hexit of 2 ascii characters represents a single encoded ascii character)
def hexbytes2ascii(hex_bytes):
    if len(hex_bytes) % 2 != 0:
        raise Exception('Invalid array of hexits, each hexit must be a 2 byte representation of an ascii char so the bytes array must have an even number of items')

    return ''.join([ hexit2ascii(ints2hexit(c[0], c[1])) for c in chunk(hex_bytes, 2) ])

def hex_string_xor_fixed(string1, string2):
    decoded1 = bytearray(binascii.a2b_hex(string1))
    decoded2 = bytearray(binascii.a2b_hex(string2))
    return ''.join([ chr(decoded1[x] ^ decoded2[x]) for x in range(0, len(decoded1)) ]).encode('hex')
