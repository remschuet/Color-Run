import random
from tkinter import *
import keyboard

# Change to 1 at 3 when you choose a color
color = 0
# Counter of point
TotalPoint = 0
# For the best score
BestScore = 0
# Timer left
TimeLeft = 20


def Timer():
    global TimeLeft
    # When time is greater then 0
    if TimeLeft >= 0:
        NewLabelTimer = TimeLeft - 1
        TimeLeft = NewLabelTimer
        LabelTimer.config(text=NewLabelTimer)
        Game.after(1000, Timer)
    # If timer = 0 timer = stop
    if TimeLeft < 0:
        ChooseWrong()


def RestartTimer():
    global TimeLeft
    # Start the game when a button will be clicked
    if keyboard.read_key() == "1":
        TimeLeft = 20
    elif keyboard.read_key() == "2":
        TimeLeft = 20
    elif keyboard.read_key() == "3":
        TimeLeft = 20


def ChooseWrong():
    global TotalPoint, BestScore, TimeLeft
    # Calcul the new are the old BestScore
    if TotalPoint >= BestScore:
        BestScore = TotalPoint
    else:
        BestScore = BestScore

    # Restart the TotalPoint to 0
    TotalPoint = 0
    # Change the TotalPoint label
    LabelCounter.config(text=TotalPoint)
    # Update the BestScore label
    LabelBestScore.config(text=BestScore)
    # Restart Time left to 20 secondes
    RestartTimer()


def AddPoint():
    global TotalPoint
    # Add point to the TotalPoint
    TotalPoint = TotalPoint + 1
    # Update the label who count TotalPoint
    LabelCounter.config(text=TotalPoint)


def CheckPoint():
    global color

    # verify if when you press red the color is red
    if LabelColor.cget("bg") == "red" and color == 1:
        AddPoint()

    # verify if when you press blue the color is blue
    elif LabelColor.cget("bg") == "blue" and color == 2:
        AddPoint()

    # verify if when you press yellow the color is yellow
    elif LabelColor.cget("bg") == "yellow" and color == 3:
        AddPoint()

    #Start Timer when turn grey
    elif LabelColor.cget("bg") == "grey":
        AddPoint()

    # If not right function to restart point and calcul BestScore
    else:
        ChooseWrong()


def ChangeColor():
    # Choose a number in range of 1 to 3
    RandomLabelColor = random.randint(1, 3)

    # If the number equal to 1 the  NewLabelColor equal to red
    if RandomLabelColor == 1:
        NewLabelColor = "red"
        NewLabelNumber = 1

    # If the number equal to 2 the  NewLabelColor equal to blue
    if RandomLabelColor == 2:
        NewLabelColor = "blue"
        NewLabelNumber = 2

    # If the number equal to 3 the  NewLabelColor equal to yellow
    if RandomLabelColor == 3:
        NewLabelColor = "yellow"
        NewLabelNumber = 3

    # Update the LabelColor to the new color
    LabelColor.config(bg=NewLabelColor)
    return NewLabelNumber


def PressKey(event=None):
    global color, TimeLeft, TotalPoint
    # For the first color, red
    if event and event.keysym in ('1'):
        color = 1
        CheckPoint()
        ChangeColor()

    # For the first color, blue
    if event and event.keysym in ('2'):
        color = 2
        CheckPoint()
        ChangeColor()

    # For the first color, yellow
    if event and event.keysym in ('3'):
        color = 3
        CheckPoint()
        ChangeColor()

    # To restart the game
    if event and event.keysym in ('s'):
        TimeLeft = 20
        LabelTimer.config(text=TimeLeft)
        TotalPoint = 0
        LabelCounter.config(text=TotalPoint)
    return color


Game = Tk()
Game.geometry("450x300")
Game.configure(background='brown')
Game.title("Game")

Game.bind('<Key>', PressKey)

# This is the label with the best score
LabelTimer = Label(Game,
                   background="grey",
                   text="20",
                   font=('Helvetica', '20'),
                   height=2,
                   width=4)
LabelTimer.pack()
LabelTimer.place(x=20, y=62)
LabelTimer.after(1000, Timer)

# This is the label who change every time
LabelColor = Label(Game,
                   background="grey",
                   height=6,
                   width=28)
LabelColor.pack()
LabelColor.place(x=120, y=53)

# This is the label with the total of the point
LabelCounter = Label(Game,
                     background="grey",
                     text="0",
                     font=('Helvetica', '20'),
                     height=1,
                     width=4)
LabelCounter.pack()
LabelCounter.place(x=195, y=1)

# This is the label with the best score
LabelBestScore = Label(Game,
                       background="grey",
                       text=BestScore,
                       font=('Helvetica', '20'),
                       height=2,
                       width=4)
LabelBestScore.pack()
LabelBestScore.place(x=350, y=62)

# Button red
ButtonRed = Button(Game,
                   text="1",
                   height=3,
                   width=6,
                   background="red",
                   font=('Helvetica', '20'))
ButtonRed.pack()
ButtonRed.place(x=10, y=170)

# Button blue
ButtonBlue = Button(Game, text="2",
                    height=3,
                    width=6,
                    background="blue",
                    font=('Helvetica', '20'))
ButtonBlue.pack()
ButtonBlue.place(x=170, y=170)

# Button yellow
ButtonYellow = Button(Game,
                      text="3",
                      height=3,
                      width=6,
                      background="yellow",
                      font=('Helvetica', '20'))
ButtonYellow.pack()
ButtonYellow.place(x=330, y=170)

LabelRestart = Label(Game,
                     background="grey",
                     text="<s> to restart",
                     font=('Helvetica', '10'),
                     height=1,
                     width=10)
LabelRestart.place(x=10, y=5)

Game.mainloop()