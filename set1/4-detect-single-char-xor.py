import support
from os import path

DATAFILE_PATH = path.join(path.dirname(path.realpath(__file__)), 'data', '4.txt')
SCORE_THRESHOLD = 100
chars = support.get_common_ascii_chars()

results = []
with open(DATAFILE_PATH) as file:
    for line in file.read().splitlines():
        decoded = support.hex2ascii(line)
        for c in chars:
            result = support.string_single_char_xor(decoded, c)
            score = support.calculate_english_language_probability_score(result)
            if score >= SCORE_THRESHOLD:
                results.append((c, score, result))
        results_sorted = sorted(results, key=lambda result: result[1], reverse=True)

    print results_sorted
