import support
import os

DATA_FILE = os.path.abspath('data/6.txt')
MIN_KEYSIZE = 2
MAX_KEYSIZE = 40

def guess_key_size(min_size, max_size, string):
    cipher_bytes = bytes(cipher_text).decode('base64')
    keysizes = range(min_size, max_size + 1)
    keysize_scores = []
    for size in keysizes:
        # Need to chunk the cipher text into pieces of length size and compare each 2 sets of them and average the distances instead of just doing the first one which is insufficient
        check_bytes1 = cipher_bytes[0:size]
        check_bytes2 = cipher_bytes[size:size*2]
        hamming_distance = support.calculate_hamming_distance(check_bytes1, check_bytes2)
        normalized_distance = hamming_distance / size
        keysize_scores.append((check_bytes1, check_bytes2, size, hamming_distance, normalized_distance))
    return keysize_scores

with open(DATA_FILE, 'r') as cipher_file:
    cipher_text = cipher_file.read()
    keysize_scores = guess_key_size(MIN_KEYSIZE, MAX_KEYSIZE, cipher_text)
    for score in keysize_scores:
        print score

EXPECTED_DISTANCE = 37
print support.calculate_hamming_distance("this is a test", "wokka wokka!!!")
print "yes" if EXPECTED_DISTANCE == support.calculate_hamming_distance("this is a test", "wokka wokka!!!") else "no"
