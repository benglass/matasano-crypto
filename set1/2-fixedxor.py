import binascii

string1  = '1c0111001f010100061a024b53535009181c'
string2  = '686974207468652062756c6c277320657965'
expected = '746865206b696420646f6e277420706c6179'

def hex_string_xor_fixed(string1, string2):
    decoded1 = bytearray(binascii.a2b_hex(string1))
    decoded2 = bytearray(binascii.a2b_hex(string2))
    return ''.join([ chr(decoded1[x] ^ decoded2[x]) for x in range(0, len(decoded1)) ]).encode('hex')

print 'true' if hex_string_xor_fixed(string1, string2) == expected else 'false'
