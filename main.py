

import turtle
import random
t1 = turtle.Turtle()
t2 = turtle.Turtle()
scrn = turtle.Screen()
t1.hideturtle()
t2.hideturtle()
turtle.screensize(500,500)
turtle.setup(520,520)
scrn.tracer(0)
t1.pensize(1)
colors=["blue","grey","white",'black','midnight blue','yellow','orange','brown']
turtle.bgcolor(colors[3])


#main function
def main():
  #outer space/ Background
  def draw_background(color):
   t1.color(color)
   for i in range(100):
    new_x = random.randint(-215,215)
    new_y = random.randint(-215,215)
  
    t1.penup()
    t1.goto(new_x, new_y)
    t1.pendown()

    c=0
    while c<5: #while loop used
      t1.lt(65)
      t1.fd(6)
      t1.lt(80)
      c = c+1
 
    #body of the ship
    '''draws rectangle'''
  def draw_rectangle(t1,x_pos,y_pos,length,width, fill_color,pencolor,heading,pensize):
    t1.penup()
    t1.goto(x_pos, y_pos)
    t1.pensize(pensize)
    t1.color(fill_color)
    t1.pencolor(pencolor)
    t1.setheading(heading)
    t1.pendown()
    t1.begin_fill()
    t1.fd(length)
    t1.lt(90)
    t1.fd(width)
    t1.lt(90)
    t1.fd(length)
    t1.lt(90)
    t1.fd(width)
    t1.end_fill()
 
      #right fin
    '''triangle'''
  def draw_triangle(t1, x_pos, y_pos, heading, fill_color,pencolor, pensize, side_length,length, hyp ):
    t1.penup()
    t1.goto(x_pos, y_pos)
    t1.pensize(pensize)
    t1.color(fill_color)
    t1.pencolor(pencolor)
    t1.setheading(heading)
    t1.pendown()
    t1.begin_fill()
    t1.fd(length)
    t1.lt(70)
    t1.fd(side_length)
    t1.lt(140)
    t1.fd(hyp)
    t1.end_fill()
  
  

#left fin
  '''triangle'''
  def draw_triangle2(t1, x_pos, y_pos, heading, fill_color,pencolor, pensize, side_length,length, hyp ):
    t1.penup()
    t1.goto(x_pos, y_pos)
    t1.pensize(pensize)
    t1.color(fill_color)
    t1.pencolor(pencolor)
    t1.setheading(heading)
    t1.pendown()
    t1.begin_fill()
    t1.fd(length)
    t1.rt(70)
    t1.fd(side_length)
    t1.rt(140)
    t1.fd(hyp)
    t1.end_fill()
    
#draws multiple circles
  '''makes the sun, the windows, and the flames'''
  def draw_circle(t1, x_pos, y_pos, heading, fill_color,pencolor, pensize,radius, extent,steps):
    t1.penup()
    t1.goto(x_pos, y_pos)
    t1.pensize(pensize)
    t1.color(fill_color)
    t1.pencolor(pencolor)
    t1.setheading(heading)
    t1.pendown()
    t1.begin_fill()
    t1.circle(radius,extent,steps)
    t1.end_fill()

#ships thruster
  '''trapezoid'''
  def draw_shape(t1, x_pos, y_pos, heading, fill_color,pencolor, pensize,s1,s2,a1,a2,s3):
    t1.penup()
    t1.goto(x_pos, y_pos)
    t1.pensize(pensize)
    t1.color(fill_color)
    t1.pencolor(pencolor)
    t1.setheading(heading)
    t1.pendown()
    t1.begin_fill()
    t1.fd(s1)
    t1.right(a1)
    t1.fd(s2)
    t1.right(a2)
    t1.fd(s3)
    t1.right(a2)
    t1.fd(s2)
    t1.end_fill()
    
#rocket ship / all shapes
  def draw_object():
    draw_rectangle(t1, 10, 160, 135, 70,colors[1],colors[3], 235, 2) 

    draw_triangle(t1, 24, 58, 235, colors[0],colors[3],2, 45,60,85)

    draw_triangle2(t1, -33, 98, 235,colors[0],colors[3],2, 45,60,85)

    draw_circle(t1,67,120,55,colors[0],colors[3],2,35,180,5000)  

    draw_circle(t1,20,101,120,colors[4],colors[3],2,20,360,4000)

    draw_circle(t1,-100, 170, 90,colors[5],colors[6],15,50,360,5000)

    draw_shape(t1,-54,40,324.5,colors[7],colors[7],2,50,30,130,50,25)

    draw_circle(t1,-83, 18, 160,colors[6],colors[6],1,25,300,2)

    draw_circle(t1,-55, -7, 190,colors[6],colors[6],1,25,300,2)

  draw_background(colors[2])
  draw_object()

  
  t2.penup()
  t2.pencolor(colors[2])
  t2.goto(100,100)
  t2.pendown()
  t2.write("Dumpster Juice")
  print('Yousef Habeeb(652622525)')


main()





