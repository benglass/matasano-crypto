string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d';

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

print hexbytes2ascii(bytearray(string)).encode('base64'),

print hex2ascii(string).encode('base64'),
