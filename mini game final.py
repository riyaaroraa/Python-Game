#Riya, Joyce, and Omar's snake game

from tkinter import *
import tkinter as tk  #importing a module that will allow us to use buttons
root=tk.Tk() #initializes an interpreter and creates a root window
class main: 
    def __init__(self,master):
        root.geometry('700x700')
        root.title('Snake Game')
        root.resizable(0,0)
        self.start()        
    def start(self): #definition that handles the start screen of the game. This will be outputted
        #on the window that was previously created-multiple buttons and titles        
        try: 
            root.rulestext.forget() 
            root.backbutton.forget()
            root.helptext.forget()
            
        except:
            pass
        root.configure(bg="light blue")
        root.titletext = tk.Label(root,text="Welcome to the Snake Game!",font=("Raleway",50), bg= "light blue")
        root.titletext.pack()
        #These are the following buttons that are created. Once they are pressed, they will go to another definition.
        #We see this part at the end of the line where it says, "command=self."
        root.startbutton = tk.Button(root,text="Start",font=("Raleway",35),bg="light blue", command=self.exit)
        root.startbutton.pack(side=tk.TOP,pady=40)
        root.rulesbutton = tk.Button(root,text="Help",font=("Raleway",35),command=self.rules) 
        root.rulesbutton.pack(side=tk.TOP,pady=40)
        
    def rules(self): #outputs the rules, how the game works
        root.titletext.forget()
        root.startbutton.forget()
        root.rulesbutton.forget()
        root.helptext = tk.Label(root,text="Help",bg="light blue",font=("Raleway",40))
        root.helptext.pack()
        root.rulestext = tk.Label(root,text="\nMake sure the snake eats the food using the keys: A, W, S, D to control the snake.\n Go back \n OR \n Close this tab to play the game.",font=("Raleway",20), bg = "light blue")
        root.rulestext.pack()
        root.backbutton = tk.Button(root,text="Back",command=self.start, bg = "black") #you will go back to the start page once you press the "back" button
        root.backbutton.pack(side=tk.BOTTOM,pady=30) #sets location of the button        
    
    def exit(self):
        root.destroy()
scr=main(root)
root.mainloop()

import turtle
import time
import random

delay = 0.08

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.setup(width=700, height=700)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("purple")
food.penup()
food.goto(0,12)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("purple")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Raleway", 35, "normal"))

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("triangle")
        new_segment.color("magenta")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score everytime snake touches food
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for collision with segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score 
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Raleway", 24, "normal"))

    time.sleep(delay)
