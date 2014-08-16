import support

string1  = '1c0111001f010100061a024b53535009181c'
string2  = '686974207468652062756c6c277320657965'
expected = '746865206b696420646f6e277420706c6179'

print 'true' if support.hex_string_xor_fixed(string1, string2) == expected else 'false'
