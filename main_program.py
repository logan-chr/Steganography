from img_gen import *
from  rle import *
import random
print('hello')


def input_img():
    mode = 'default'
    letters = ['r','o','y','g','b','i','p','w']
    inp = ()
    flag = True
    string1 = ('')
    while flag == True:
        if mode == 'default':
        
            inp = input()
            for i in range(len(inp)):
                if inp[i] in colours:
                    string1 += inp[i]
                if inp == 'auto':
                    mode = 'auto'
                if inp[i] == -1:
                    flag=  False
        else:
            for i in range(24*24):
                a = letters[random.randint(0,7)]
                print(a)
                string1 += a
            flag = False
    return string1


code = compress_image(input_img())
generate_image(code)