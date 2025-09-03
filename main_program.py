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
            print('ii')
            inp = str(input('print:'))
            print(inp[:6])
            print(inp[7:])
            if inp[:6] == 'preset':
                    print('p')
                    if inp[7:]== 'sky':
                        print('h')
                        strinv=('bbbbwwbbbbbbbbbbbbbbbbbb'+
                                'bbbwwwwwwbwwbbbbbbbyyybb'+
                                'bbbbwwwwwwwwbbbbbbbyyybb'+
                                'bbbbbbbbbbbbbbbbbbbyyybb'+
                                'bbbbbbbbbbbbbbbbbbbbbbbb'+
                                'bbbbbbbbbbbbbbbbbbbbbbbb'+
                                'bbbbbbbbbbbbbbbbbbbbbbbb'+
                                'bbbbbbbwwbbbbbbbbbbbbbbb'+
                                'bbbbbbwwwwbbbbbbbbbbbbbb'+
                                'bbbwwwwwwwwbbbbbbbbbbbbb'+
                                'bbbbbbbbbbbbbbbbbbbgggbb'+
                                'bbbbbbbbbbbbbwwwbbbgggbb'+
                                'bbbbbbbbbbbbwwwbbbbbpbbb'+
                                'ggbbbbbbbbbbbbbbbbbggggg'+
                                'ggggbbbbbbbbggggggggggg'+
                                'gggggggggggggggggggggggg'+
                                'gggggggggggggggggggggggg'+
                                'gggggggggggggggggggggggg'+
                                'gggggggggggggggggggggggg'+
                                'gggggggggggggggggggggggg'+
                                'gggggggggggggggggggggggg'+
                                'gggggggggggggggggggggggg')
                        string1 = strinv
                        flag = False
                        print('hi')
            else:
                
                for i in range(len(inp)):
                    if inp[i] in colours:
                        string1 += inp[i]
                    if inp == 'auto':
                        mode = 'auto'
                    if inp[i] == -1:
                        flag=  False
    
        else:
            while len(string1)< 24**2:
                a = letters[random.randint(0,7)]
                print(a)
                string1 += a
            flag = False
    return string1

secret = ('11111111')
code = compress_image(input_img())
generate_image(code)



