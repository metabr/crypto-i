#!/usr/bin/env python

from Crypto.Cipher import AES
from Crypto import Random

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in
            zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for
            (x, y) in zip(a, b[:len(a)])])

def decrypt_cbc(key, ct):
    cipher = AES.AESCipher(key)

    c = []
    m = []

    for i in range(0, len(ct)):
        if i % 16 == 0:
            c.append("")
        c[-1] += ct[i]

    for i in range(0, len(c) - 1):
        iv = c[i]
        m.append(strxor(cipher.decrypt(c[i+1]), iv))

    d = ''.join(m)
    padded = ord(d[-1])
    return d[0:-padded]

def inc_iv(iv):
    iv_h = iv.encode("hex")
    iv_i = int(iv_h, 16)
    iv_i += 1
    iv_h = "%032x" % iv_i
    return iv_h.decode("hex")

def decrypt_ctr(key, ct):
    cipher = AES.AESCipher(key)

    c = []
    m = []

    for i in range(0, len(ct)):
        if i % 16 == 0:
            c.append("")
        c[-1] += ct[i]

    iv = c[0]
    for i in range(1, len(c)):
        m.append(strxor(cipher.encrypt(iv), c[i]))
        iv = inc_iv(iv)

    return ''.join(m)

key_cbc = "140b41b22a29beb4061bda66b6747e14".decode("hex")
ct_1 = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81".decode("hex")
ct_2 = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253".decode("hex")

print decrypt_cbc(key_cbc, ct_1)
print decrypt_cbc(key_cbc, ct_2)

key_ctr = "36f18357be4dbd77f050515c73fcf9f2".decode("hex")
ct_3 = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329".decode("hex")
ct_4 = "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451".decode("hex")

print decrypt_ctr(key_ctr, ct_3)
print decrypt_ctr(key_ctr, ct_4)
