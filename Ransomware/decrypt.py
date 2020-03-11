
import os
import hashlib
from Crypto.Cipher import AES
import struct

def decrypt(encfile):
  private_key = hashlib.sha256("password".encode("utf-8")).digest()
  sz = 2048
  with open(encfile, 'rb') as fin:
    fsz = struct.unpack('<Q', fin.read(struct.calcsize('<Q')))[0]
    iv = fin.read(16)
    aes = AES.new(private_key, AES.MODE_CBC, iv)
    with open(encfile+".jpg", 'wb') as fout:
      while True:
        data = fin.read(sz)
        n = len(data)
        if n == 0:
          break
        decd = aes.decrypt(data)
        n = len(decd)
        if fsz > n:
          fout.write(decd)
        else:
          fout.write(decd[:fsz]) # <- remove padding on last block
        fsz -= n


decrypt('/tmp/prueba1/mimounstrito1.jpg.enc')