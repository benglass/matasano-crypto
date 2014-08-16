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

def string_single_char_xor(string, char):
    stringbytes = bytearray(string)
    xord = [ chr(b ^ ord(char)) for b in stringbytes ]
    return ''.join(xord)

CHAR_FREQUENCY_WEIGHTS = [
    ('e',13.0001),
    ('t',9.056),
    ('a',8.167),
    ('o',7.507),
    ('i',6.966),
    ('n',6.749),
    ('s',6.327),
    ('h',6.094),
    ('r',5.987),
    ('d',4.253),
    ('l',4.025),
    ('c',2.782),
    ('u',2.758),
    ('m',2.406),
    ('w',2.360),
    ('f',2.228),
    ('g',2.015),
    ('y',1.974),
    ('p',1.929),
    ('b',1.492),
    ('v',0.978),
    ('k',0.772),
    ('j',0.153),
    ('x',0.150),
    ('q',0.095),
    ('z',0.074)
]

def score_string_by_char_freq(string, weights):
    score = 0
    for x in weights:
        char, weight = x
        score += weight * string.count(char)

    return score

def calculate_english_language_probability_score(string):
    if string.count(' ') == 0:
        return 0

    return score_string_by_char_freq(string, CHAR_FREQUENCY_WEIGHTS)
