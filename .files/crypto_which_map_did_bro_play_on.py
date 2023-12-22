from Crypto.Cipher import AES
from random import*
import datetime
import base64
#pip install pycryptodome

flag = b"flag"
iv = b"\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"
block_size = 16
flag = flag.ljust((len(flag) + block_size - 1) // block_size * block_size, b"\0")
time = datetime.datetime.now()
print("Map generated on " + str(time))


map_seed = int(round((time.timestamp() * 10000),0))
seed(map_seed)


key = []
for i in range(24):
    key.append(randint(0,255))

keyBytes = bytes(key)


cipher = AES.new(keyBytes,AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(flag)
encrypted_flag = base64.b64encode(ciphertext).decode('utf-8')

print("Encrypted flag: " + encrypted_flag)
