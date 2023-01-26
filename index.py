from RSA import *

p = 779849711281
q = 748173698927
e = 1018651
n = p * q
message = 'Hello'

rsa = RSA(p, q, e)
ciphertext = rsa.encrypt(message)
print(ciphertext)

plaintext = rsa.decrypt(ciphertext)
print(plaintext)
