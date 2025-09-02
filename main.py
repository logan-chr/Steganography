from img_gen import *
from  rle import *

def input_img():
    while inp != '-1':
        inp = input()
        if inp in colours:
            print(inp)

print('h')
input_img()
code = compress_image(string1)
generate_image(code)