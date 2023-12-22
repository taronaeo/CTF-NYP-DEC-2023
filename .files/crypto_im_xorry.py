flag=""
key=""
key_len=4

def encrypt(flag,key):
    key_long=(key * (len(flag)//len(key)))[:len(flag)]
    encrypted=result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ ord(k)), flag, key_long))

    return encrypted
result="".join(encrypt(flag,key))
print(f'Output: {result}') #Cough cough Output: 2c38321e1250030c0c153a4e032103111600010e091c
