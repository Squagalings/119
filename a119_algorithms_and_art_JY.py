import turtle as trtl
import math

wn = trtl.Screen()
t = trtl.Turtle()
t.speed(0)
t.hideturtle()
wn.tracer(0)

# array of colors
t_colors = ["red","orange","yellow","green","blue","purple"]


def draw_ring(radius):
    if radius<1:
        return
    
    ind = 0
    
    # template circle
    # t.penup()
    # t.goto(0,-50)
    # t.pendown()
    # t.circle(50)
    # t.penup()

    # looping circles
    for theta in range(-90,270,10):
        # converting x,y to r, theta
        a=math.radians(theta+90)
        
        xpos = 50*math.cos(a)
        ypos = 50*math.sin(a)

        t.penup()
        t.goto(xpos, ypos)
        t.setheading(theta)
        t.pencolor(t_colors[ind%6]) # so every 6 it resets
        t.pendown()
        t.circle(radius)
        ind+=1

# zooming in
zoom_offset=0

while True:
    t.clear()
    zoom_offset+=7

    if zoom_offset >=50:
        zoom_offset=0
    
    for i in range(1,6):
        current_r=(i*50)+zoom_offset
        draw_ring(current_r)
    wn.update()



wn.mainloop()
