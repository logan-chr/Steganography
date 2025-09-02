

def rle(data):
    string = []
    counter = 1
    data+= (' ')
    for i in range(len(data)):
        if i != len(data)-1:
            if data[i] == data[i+1]:
                
                counter +=1
            else:
                string.append(str(counter)+str(data[i]))
                counter = 1
    return string

def steg_encode(data,secret):
    string = []
    counter = 1
    j = 0
    data+= (' ')
    for i in range(len(data)):
        if i != len(data)-1:
            if str(j) ==secret[j]:
                j=int(0)
                string.append('s')
            else:
                j+= 1
            if data[i] == data[i+1]:
                
                counter +=1
            else:
                string.append(str(counter)+str(data[i]))
                counter = 1
    return string



def compress_image(image_data):
    return rle(image_data)


IMAGE = ('bbbbbbbbbbbbbrrrrggppooooyyyrrryryrypopgpgggpppgggpppbbrpg')

print(compress_image(IMAGE))