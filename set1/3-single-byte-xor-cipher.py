import support
import binascii

encoded = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
decoded = binascii.a2b_hex(encoded)

chars = support.get_common_ascii_chars()

results = []

for c in chars:
    result = support.string_single_char_xor(decoded, c)
    score = support.calculate_english_language_probability_score(result)
    results.append((c, score, result))

results_sorted = sorted(results, key=lambda result: result[1], reverse=True)

for res in results_sorted:
    print res
