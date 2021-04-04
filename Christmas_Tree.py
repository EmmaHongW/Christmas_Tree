# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import turtle as t
t.TurtleScreen._RUNNING = True
screen = t.Screen()
screen.setup(800,700)
circle = t.Turtle()
circle.shape = ('circle')
circle.color('red')
circle.speed('fastest')
circle.up()
square = t.Turtle()
square.shape('square')
square.color('green')
square.speed('fastest')
square.up()
circle.goto(0,280)
circle.stamp()
k = 0
for i in range(1,17):
    y = 30*i
    for j in range(i-k):
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()
    if i%4 == 0:
        x = 30*(j+1)
        circle.color('pink')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp()
        k += 2
    if i%4 == 3:
        x = 30*(j+1)
        circle.color('yellow')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp()
square.color('brown')
for i in range(17,20):
    y = 30*i
    for j in range(3):
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()
t.goto(-250,0)
wish_word = ("Merry Christmas to You!") # You may change the word you into something else
t.color('red')
t.write(wish_word,font= ("Freestyle Script",30,'bold'))
t.done()
        
        
        
    