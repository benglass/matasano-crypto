import support
import binascii

string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

guesses = support.guess_string_single_char_xor(
        binascii.a2b_hex(string),
        support.get_common_ascii_chars()
    )

for guess in guesses:
    print guess
