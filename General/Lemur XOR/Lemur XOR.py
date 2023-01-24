from PIL import Image
from pwn import xor

lemur = Image.open('lemur.png')
flag = Image.open('flag.png')
crypto=Image.frombytes(flag.mode, flag.size,  xor(lemur.tobytes(), flag.tobytes()))
crypto.save("result.png")