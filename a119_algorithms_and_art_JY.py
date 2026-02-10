import turtle as trtl
import math

wn = trtl.Screen()
t = trtl.Turtle()
t.speed(0)
t.hideturtle()
wn.tracer(0) # tracer updates the screen every iteration.

# array of colors
t_colors = ["red","orange","yellow","green","blue","purple"]


# one ring of circles
def draw_ring(radius):
    
    ind = 0 # this is the index for the t_colors array. Right now it's preset at red.
    
    # looping circles
    for theta in range(-90,270,10): # this is for each ring of circles. It starts at the bottom at -90 degrees and goes up to +270 which is a full circle
        
        a=math.radians(theta+90) # +90 because the turtle's 0 degrees (north) and the math 0 degrees (east) is different
        
        # converting polar coordinates to cartesian bc python can't do polar
        xpos = 50*math.cos(a)
        ypos = 50*math.sin(a)

        # the actual drawing part when all the stuff is calculated
        t.penup()
        t.goto(xpos, ypos)
        t.setheading(theta)
        t.pencolor(t_colors[ind%6]) # so every 6 it resets
        t.pendown()
        t.circle(radius)
        ind+=1

# zooming in
zoom_offset=0 # this is how much the radius of the circles have grown from their default size

while True:
    t.clear() # we clear the screen and replace with the updated circles that are bigger
    zoom_offset+=7 # circles grow by 7 pixels every time it updates

    if zoom_offset >=50: # the radius of each ring of circles is 50px apart so when it zooms in to 50 px, we can reset it
        zoom_offset=0
    
    for i in range(1,6): # from 1 to 5 we multiply by 50 so we get rings of size 50, 100...250
        current_r=(i*50)+zoom_offset # this is the size of the rings, not the circle
        draw_ring(current_r)
    wn.update()
