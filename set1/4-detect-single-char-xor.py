import support
from os import path
import sys

DATAFILE_PATH = path.join(path.dirname(path.realpath(__file__)), 'data', '4.txt')
chars = support.get_common_ascii_chars()

results = []
with open(DATAFILE_PATH) as file:
    for line in file.read().splitlines():
        guess = support.guess_string_single_char_xor(
                support.hex2ascii(line),
                chars
            )[:1]
        if guess:
            print guess
            sys.exit()
