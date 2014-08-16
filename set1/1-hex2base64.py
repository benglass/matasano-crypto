import support

string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d';
expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

print 'true' if support.hexbytes2ascii(bytearray(string)).encode('base64') else 'false',

print 'true' if support.hex2ascii(string).encode('base64') else 'false',
