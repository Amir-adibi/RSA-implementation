
class RSA:
    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.e = e

        self.n = p * q
        self.phi = (p-1) * (q-1)
        self.d = self.invert_modulo(self.e, self.phi)

    def encrypt(self, message):
        exponent = self.e
        modulo = self.n
        
        return self.pow_mod(self.convert_to_int(message), exponent, modulo)

    def decrypt(self, ciphertext):
        exponent = self.d
        modulo = self.n

        return self.convert_to_str(self.pow_mod(ciphertext, exponent, modulo))

    def pow_mod(self, a, n, modulo):  # Calculates a^n mod 'modulo'
        if n == 0:
            return 1 % modulo
        elif n == 1:
            return a % modulo
        else:
            b = self.pow_mod(a, n // 2, modulo)
            b = b * b % modulo
            if n % 2 == 0:
                return b
            else:
                return b * a % modulo

    def extended_euclid(self, a, b):  # Calculates coefficients of a and b as xa + yb = gcd(a, b)
        if b == 0:
            return 1, 0
        (x, y) = self.extended_euclid(b, a % b)
        k = a // b
        return y, x - k * y

    def invert_modulo(self, a, n):  # Calculates inversion of a
        (b, x) = self.extended_euclid(a, n)
        if b < 0:
            b = (b % n + n) % n
        return b

    @staticmethod
    def convert_to_int(message_str):
        res = 0
        for i in range(len(message_str)):
            res = res * 256 + ord(message_str[i])
        return res

    @staticmethod
    def convert_to_str(n):
        res = ""
        while n > 0:
            res += chr(n % 256)
            n //= 256
        return res[::-1]
