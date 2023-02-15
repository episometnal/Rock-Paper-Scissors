from tkinter import *
from PIL import ImageTk,Image
import random

values = ["ROCK", "PAPER", "SCISSORS"]
score_player = 0
score_computer = 0

def transition():
    ds = "..."
    space.config(text="ROCK")
    space.after(300)
    space.update()
    space.config(text=ds)
    space.after(300)
    space.update()
    space.config(text="PAPER")
    space.after(500)
    space.update()
    space.config(text=ds)
    space.after(300)
    space.update()
    space.config(text="SCISSORS")
    space.after(300)
    space.update()
    space.config(text="")
    space.after(400)
    space.update()



def ifRock():
    global score_player,score_computer
    choice = str(random.choice(values))
    transition()

    if choice == "ROCK":
        result.config(text="DRAW")
        computer.config(image=image_rock)
    elif choice == "PAPER":
        result.config(text="LOST")
        computer.config(image=image_paper)
        score_computer += 1
        computer_score.config(text=score_computer)
    else:
        result.config(text="WIN")
        computer.config(image=image_scissors)
        score_player += 1
        player_score.config(text=score_player)
    player.config(image=image_rock)

def ifPaper():
    global score_player,score_computer
    choice = str(random.choice(values))
    transition()

    if choice == "ROCK":
        result.config(text="WIN")
        computer.config(image=image_rock)
        score_player += 1
        player_score.config(text=score_player)

    elif choice == "PAPER":
        result.config(text="DRAW")
        computer.config(image=image_paper)
    else:
        result.config(text="LOST")
        computer.config(image=image_scissors)
        score_computer += 1
        computer_score.config(text=score_computer)

    player.config(image=image_paper)

def ifScissors():
    global score_player,score_computer
    choice = str(random.choice(values))
    transition()

    if choice == "ROCK":
        result.config(text="LOST")
        computer.config(image=image_rock)
        score_computer += 1
        computer_score.config(text=score_computer)
    elif choice == "PAPER":
        result.config(text="WIN")
        computer.config(image=image_paper)
        score_player += 1
        player_score.config(text=score_player)
    else:
        result.config(text="DRAW")
        computer.config(image=image_scissors)
    player.config(image=image_scissors)

def restart():
    global score_player,score_computer
    score_player = 0
    score_computer = 0
    player_score.config(text=score_player)
    computer_score.config(text=score_computer)
    player.config(image=image_user)
    computer.config(image=image_robot)
    result.config(text="RESULT")


win = Tk()
win.title("ROCK PAPER SCISSORS")
win.geometry("700x500")

#Labels
Label(win, text=" ROCK PAPER SCISSORS ",fg="black",font="Normal 22 bold").pack(pady=30)

frame = Frame(win)
frame.pack()

l1 = Label(frame, text="Player",width=15, font=10, fg="#D35400")
l2 = Label(frame, text="VS", width=13, font=10)
l3 = Label(frame, text="Computer", width=15, font=10, fg="#C0392B")
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

frame2 = Frame(win)
frame2.pack()

player_score = Label(frame2, text=score_player,font=30, fg="white", bg="black",width=5)
computer_score = Label(frame2, text=score_computer, font=30, fg="white", bg="black", width=5)
player_score.pack(side=LEFT,padx=130)
computer_score.pack(padx=130,pady=5)

path_user = "user.png"
path_robot = "robot.png"
path_rock = "rock.png"
path_paper = "paper.png"
path_scissors = "scissors.png"

image_rock = ImageTk.PhotoImage(Image.open(path_rock).resize((100, 100), Image.LANCZOS))
image_paper = ImageTk.PhotoImage(Image.open(path_paper).resize((100, 100), Image.LANCZOS))
image_scissors = ImageTk.PhotoImage(Image.open(path_scissors).resize((100, 100), Image.LANCZOS))
image_user = ImageTk.PhotoImage(Image.open(path_user).resize((100,100), Image.LANCZOS))
image_robot = ImageTk.PhotoImage(Image.open(path_robot).resize((100,100), Image.LANCZOS))

frame3 = Frame(win)
frame3.pack()

player = Label(frame3, image=image_user, bg="#ABEBC6", height=110)
space = Label(frame3, height=6, width=21, font="normal 12 bold italic")
computer = Label(frame3, image=image_robot, bg="#F8C471", height=110)
player.pack(side=LEFT)
space.pack(side=LEFT)
computer.pack()

result = Label(win,text="...", font=100, borderwidth=2, relief="solid", width=15, bg="grey")
result.pack()


frame4 = Frame(win)
frame4.pack()

b1 = Button(frame4, text="ROCK", width=30, height=5, command=ifRock)
b2 = Button(frame4, text="PAPER", width=30, height=5, command=ifPaper)
b3 = Button(frame4, text="SCISSORS", width=30, height=5, command=ifScissors)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(pady=10)


frame5 = Frame(win)
frame5.pack()

bRestart = Button(frame5, text="RESTART", width=15, height=2, bg="blue", command=restart)
bExit = Button(frame5, text="EXIT", width=15, height=2, bg="red", command=win.destroy)
bRestart.pack(side=LEFT)
bExit.pack()


win.mainloop()
