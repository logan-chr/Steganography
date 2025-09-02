import turtle

code1 = ['13b', '4r', '2g', '2p', '4o', '3y', '3r', '1y', '1r', '1y', '1r', '1y', '1p', '1o', '1p', '1g', '1p', '3g', '3p', '3g', '3p', '2b', '1r', '1p', '1g']
def generate_image(code):
    colours = {
    'r':'red',
    'o':'orange',
    'y':'yellow',
    'g':'green',
    'b':'blue',
    'i':'indigo',
    'p':'purple'
    }
    list = []
    for i in range(len(code)):
        for j in range(int(code[i][:-1])):
            list.append(colours[code[i][-1:]])
    pen = turtle.Turtle()

    pen.speed(1000)
    count = 0
    for i in range(24):
     
      # not ready to draw
      pen.up()
     
      # set position for every row
      pen.setpos(-360, 309+30 * -i)
     
      # ready to draw
      pen.down()
     
      # row
      for j in range(24):
        count+=1
        print(count)
        # conditions for alternative color
        try:
            col = list[count]
        except:
           col = 'white'

          
     
        # fill with given color
        pen.fillcolor(col)
     
        # start filling with colour
        pen.begin_fill()
     
        # call method
        for i in range(4):
            pen.forward(30)
            pen.left(90)
 
        pen.forward(30)
        # stop filling
        pen.end_fill()

generate_image(code1)