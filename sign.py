from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os
load_dotenv()

def sign(slice1,slice2,slice3,slice4):
    pieces = [slice1, slice2, slice3, slice4]
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
