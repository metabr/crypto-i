#!/usr/bin/env python

import os
from Crypto.Hash import SHA256


f = os.open('/Users/br/Downloads/file2.mp4', os.O_RDONLY)

fb = []

r = os.read(f, 1024)
while r != "":
    fb.append(r)
    r = os.read(f, 1024)

h = SHA256.new()
h.update(fb[-1])
h_t = h.digest()
for b in reversed(fb[0:-1]):
    t = b.encode("hex") + h_t.encode("hex")
    h = SHA256.new()
    h.update(t.decode("hex"))
    h_t = h.digest()

print h.hexdigest()
