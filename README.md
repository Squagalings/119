# 1.1.9 Algorithms and Art
This project uses circles and turtles to draw a spirograph. Functions like for loops, if statements, while True loops were used. Libraries that were used were turtle and math from Python.

The tracer module draws everything out first (like each frame) before showing it so it looks like it was instantly there. It does this with every iteration so it appears like the radius is growing, like frame-by-frame animation.

## Tracer
According to [StackOverflow]https://stackoverflow.com/questions/62613041/what-does-turtle-tracer-do, "Generally, the computer can draw graphics instantaneously. Displaying every drawing update on the screen, and slowing down these updates, so we can see them, is tracing in turtle graphics.
The python `tracer()` function turns automatic screen updates on or off -- on by default -- and also sets the `update()` delay. In Python 2, the first argument to `tracer()` is boolean, `True` to have automatic screen updates on, `False` to turn them off. 

## Planning sketch →
This was essentially what I was planning to make: https://www.geogebra.org/resource/fq2wxepb/UQ5JtjFYPKhXWyqr/material-fq2wxepb.png

## Breakdown:
- Import turtle and math
- Figure out how to make a circle of circles conceptually. Find a way to convert polar to cartesian coordinates.
- Start with a base circle outlined in black, then draw circles of the same radius around it.
- After that copy the same code and change the radius to 100
- Add 2-3 more rings with radius increments of +50
- Add tracer and update lines (2 lines)
- Make an array with 6-7 colors
- Delete all the code for the rings and use a function that changes with radius, so you can draw rings of 50, 100, … 250.
- The function which is a for loop from (-90,270,10) starts at -90 degrees ends at 270 and each circle within a ring shifts by 10 degrees. After every circle set the pen color to the next element in the color array.
- Create a var called zoom_offset that increases the radius of the rings and circles by 7 each iteration.
- Use a while True loop to call the function from step 6, using a current radius instead of the radius argument
- Update current radius with a for i in range 1 to 6, (1-5 inclusive) (i*50) + zoom_offset
- That is how big your radius will be each iteration. And each ring changes together because you multiply by 50 and zoom_offset changes together. So there’s always 50px radius difference in between the circles.

## Pseudocode:
``` python
Import turtle as trtl
Import math
.
# setup stuff here
.
# colors array
Colors array = [red, orange, yellow, etc.]

Draw circle function(radius):
	Conditional 
	If radius<1:
		return
	
	Index of colors array = 0

	Iteration
	For loop for theta from -90 to 270, increment 10 degrees 
		a=angle for turtle position in radians+90
		X position = 50cos(a)
		Y position = 50sin(a)  # because Python math uses radians, but setheading is in degrees
		(insert whole thing with turtle going to xposition yposition, facing theta(degrees), draw circle with radius, and index+=1
	
# zooming in
Zoom_offset = 0

This technically counts as movement
While True:
	Clear canvas every time
	Zoom_offset +=7 # this is how fast the circles are growing
	If zoom offset is greater than 50:  # then it overlaps with the initial image
		Zoom offset = 0 # we can reset it so it’s the same as the initial image

	For i in range(1,6)
		Current radius = (i*50)+zoom offset # you get rings of circles at 50, 100, 150, etc. to 250 and they all expand at the same time by the zoom offset

	wn.update() # just updates the window every iteration
```
