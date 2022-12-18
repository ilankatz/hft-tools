from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os
load_dotenv()

def sign(slice1,slice2,slice3,slice4):
    crypt1 = slice1[1:121]
    dec1 = slice1[121:167]
    crypt2 = slice2[1:121]
    dec2 = slice2[121:167]
    crypt3 = slice3[1:121]
    dec3 = slice3[121:167]
    crypt4 = slice4[1:121]
    dec4 = slice4[121:167]
    decrypt1 = Fernet(dec4)
    slice1 = decrypt1.decrypt(crypt1).decode()
    decrypt2 = Fernet(dec1)
    slice2 = decrypt2.decrypt(crypt2).decode()
    decrypt3 = Fernet(dec2)
    slice3 = decrypt3.decrypt(crypt3).decode()
    decrypt4 = Fernet(dec3)
    slice4 = decrypt4.decrypt(crypt4).decode()
    slices = [slice2, slice1, slice3, slice4]
    slices.sort()
    fullKey = ''
    for slice in slices:
        fullKey = fullKey + slice[1:]
    return fullKey

key = os.getenv('key1')

slice1 = key[0:16]
slice2 = key[16:32]
slice3 = key[32:48]
slice4 = key[48:64]


slices = slice1 + slice2 + slice3 + slice4
slice1 = '1' + slice1
slice2 = '2' + slice2
slice3 = '3' + slice3
slice4 = '4' + slice4
fernet1 = Fernet(os.getenv('fernetKey1'))
fernet2 = Fernet(os.getenv('fernetKey2'))
fernet3 = Fernet(os.getenv('fernetKey3'))
fernet4 = Fernet(os.getenv('fernetKey4'))

enc1 = '2' + fernet1.encrypt(slice1.encode()).decode('utf-8') + os.getenv('fernetKey2')
enc2 = '3' + fernet2.encrypt(slice2.encode()).decode('utf-8') + os.getenv('fernetKey3')
enc3 = '4' + fernet3.encrypt(slice3.encode()).decode('utf-8') + os.getenv('fernetKey4')
enc4 = '1' + fernet4.encrypt(slice4.encode()).decode('utf-8') + os.getenv('fernetKey1')

print(sign(enc1,enc2,enc3,enc4) == os.getenv('key1'))
