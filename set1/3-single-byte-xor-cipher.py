import support
import binascii

encoded = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
decoded = binascii.a2b_hex(encoded)
chars = list(map(chr, range(30, 123)))

char_frequency_weights = [
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

def score_result(string):
    if result.count(' ') == 0:
        return 0

    return score_string_by_char_freq(string, char_frequency_weights)

# Crude solution just brute force xors against all ascii characters from 0 through Z, then you have to examine the output to see what looks like decoded string
results = []

for c in chars:
    result = support.string_single_char_xor(decoded, c)
    score = score_result(result)
    results.append((c, score, result))

results_sorted = sorted(results, key=lambda result: result[1], reverse=True)

for res in results_sorted:
    print res
