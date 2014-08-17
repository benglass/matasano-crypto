import support
from itertools import cycle

CLEARTEXT = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
EXPECTED = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""
KEY = 'ICE'
KEYS = cycle(KEY)

encrypted = []
for char in CLEARTEXT:
    k = next(KEYS)
    encrypted.append(support.string_single_char_xor(char, k))

print ''.join(encrypted).encode('hex')
print EXPECTED
