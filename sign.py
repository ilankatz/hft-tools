from cryptography.fernet import Fernet
from dotenv import load_dotenv
import dotenv
import os
import random
load_dotenv()

def sign(slices):
    pieces = []
    secret = os.getenv('secretCharacter')
    for piece in slices:
        pos = piece[secret]
        f = piece[0:secret]
        s = piece[secret+1:]
        slice = pos + f + s
        pieces.append(slice)
    pieces.sort()
    crypts = []
    decs = []
    for piece in pieces:
        crypts.append(piece[1:121])
        decs.append(piece[121:167])
        
    fernets = []
    for dec in decs:
        fernets.append(Fernet(dec))
    order = [3,0,1,2]
    fernets[:] = [fernets[i] for i in order]
    slices = []

    for i in range(len(fernets)):
        cur = fernets[i].decrypt(crypts[i]).decode()
        slices.append(cur)
    slices.sort()
    fullKey = ''
    for slice in slices:
        fullKey = fullKey + slice[1:]
    return fullKey

def encrypt(key):
    slice1 = key[0:16]
    slice2 = key[16:32]
    slice3 = key[32:48]
    slice4 = key[48:64]

    slice1 = '1' + slice1
    slice2 = '2' + slice2
    slice3 = '3' + slice3
    slice4 = '4' + slice4

    key1 = Fernet.generate_key()
    key2 = Fernet.generate_key()
    key3 = Fernet.generate_key()
    key4 = Fernet.generate_key()

    fernet1 = Fernet(key1)
    fernet2 = Fernet(key2)
    fernet3 = Fernet(key3)
    fernet4 = Fernet(key4)

    enc1 = fernet1.encrypt(slice1.encode()).decode('utf-8') + key2.decode()
    enc2 = fernet2.encrypt(slice2.encode()).decode('utf-8') + key3.decode()
    enc3 = fernet3.encrypt(slice3.encode()).decode('utf-8') + key4.decode()
    enc4 = fernet4.encrypt(slice4.encode()).decode('utf-8') + key1.decode()
    secret = os.getenv('secretCharacter')
    enc1 = enc1[:secret] + '2' + enc1[secret:]
    enc2 = enc2[:secret] + '3' + enc2[secret:]
    enc3 = enc3[:secret] + '4' + enc3[secret:]
    enc4 = enc4[:secret] + '1' + enc4[secret:]
    slices = [enc1,enc2,enc3,enc4]
    random.shuffle(slices)
    return slices

def updateenv(slices, envvars):
    if len(envvars) != 4:
        print("you must give a list of 4 env variable names. You have provided " + str(len(envvars)) + ".")
        return False
    if len(slices) != 4:
        print("you must give a list of 4 slices. You have provided " + str(len(slices)) + ".")
        return False

    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)
    for i in range(4):
        dotenv.set_key(dotenv_file, envvars[i], slices[i])
    print("Updated!")
