

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_keys():
    p, q = 7919, 1009
    n = p * q
    phi = (p - 1) * (q - 1)
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break
    d = mod_inverse(e, phi)
    return e, d, n

def encrypt(m, e, n):
    return pow(m, e, n)

def decrypt(c, d, n):
    return pow(c, d, n)

if __name__ == "__main__":
    e, d, n = generate_keys()
    print(f"Public Key: ({e}, {n})")
    print(f"Private Key: ({d}, {n})")

    M = 123
    print(f"Original Message: {M}")

    C = encrypt(M, e, n)
    print(f"Encrypted Message: {C}")

    decrypted = decrypt(C, d, n)
    print(f"Decrypted Message: {decrypted}")
