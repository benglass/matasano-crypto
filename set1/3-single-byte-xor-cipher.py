import support
import binascii

encoded = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
decoded = binascii.a2b_hex(encoded)
chars = list(map(chr, range(30, 123)))

# Crude solution just brute force xors against all ascii characters from 0 through Z, then you have to examine the output to see what looks like decoded string
for c in chars:
    print (c, support.string_single_char_xor(decoded, c))
