import turtle
list = ['red','orange','yellow','green','blue','indigo','purple','black']
pen = turtle.Turtle()

pen.speed(1000)
for i in range(8):
    for i in range(24):
     
      # not ready to draw
      pen.up()
     
      # set position for every row
      pen.setpos(-360, 309+30 * -i)
     
      # ready to draw
      pen.down()
     
      # row
      for j in range(24):
        
        # conditions for alternative color
        try:
            col = list[j]
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