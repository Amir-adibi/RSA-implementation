
# import timeit
# code = """
class RSA:
    def encrypt(self, message, modulo, exponent):
        return self.powMod(self.convertToInt(message), exponent, modulo)

    def decrypt(self, ciphertext, p, q, exponent):
        phi = (p - 1) * (q - 1)
        d = self.invertModulo(exponent, phi)
        return self.convertToStr(self.powMod(ciphertext, d, p * q))

    def powMod(self, a, n, mod): #Calculates a^n mod 'mod'
        if n == 0:
            return 1 % mod
        elif n == 1:
            return a % mod
        else:
            b = self.powMod(a, n // 2, mod)
            b = b * b % mod
            if n % 2 == 0:
                return b
            else:
                return b * a % mod

    def extendedEuclid(self, a, b): #Calculates coefficients of a and b as xa + yb = gcd(a, b)
        if b == 0:
            return (1, 0)
        (x, y) = self.extendedEuclid(b, a % b)
        k = a // b
        return (y, x - k * y)

    def invertModulo(self, a, n): #Calculates invertion of a
        (b, x) = self.extendedEuclid(a, n)
        if b < 0:
            b = (b % n + n) % n
        return b

    def convertToInt(self, message_str):
        res = 0
        for i in range(len(message_str)):
            res = res * 256 + ord(message_str[i])
        return res

    def convertToStr(self, n):
        res = ""
        while n > 0:
            res += chr(n % 256)
            n //= 256
        return res[::-1]

p = 779849711281
q = 748173698927
e = 1018651
n = p * q
message = 'Hello'

rsa = RSA()

print(n)
ciphertext = rsa.encrypt(message, n, e)
print(ciphertext)

plaintext = rsa.decrypt(ciphertext, p, q, e)
print(plaintext)
# """

# execution_time = timeit.timeit(code, number=1)
# print(execution_time, 's')

