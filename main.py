def rle(data):
    string = []
    counter = 1
    data+= (' ')
    for i in range(len(data)):
        if i != len(data)-1:
            print(data[i])
            if data[i] == data[i+1]:
                
                counter +=1
            else:
                string.append(str(counter)+str(data[i]))
                counter = 1
    return string



print(rle('assjsssssaaanaabbm'))