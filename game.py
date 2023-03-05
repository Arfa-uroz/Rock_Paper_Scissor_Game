from tkinter import *
from random import randint

#PIL is the pillow to add images in the GUI
from PIL import Image, ImageTk

root = Tk()
root.title("Game")
root.config(bg="#fff6b0")

#Loading all the images in the program
rock1 = ImageTk.PhotoImage(Image.open(r"D:\Python_Programs\projectRPSgame\img1.png"))
rock2 = ImageTk.PhotoImage(Image.open(r"D:\Python_Programs\projectRPSgame\rockR.png"))
paper1 = ImageTk.PhotoImage(Image.open(r"D:\Python_Programs\projectRPSgame\paper.png"))
paper2 = ImageTk.PhotoImage(Image.open(r"D:\Python_Programs\projectRPSgame\paperR.png"))
scissor1 = ImageTk.PhotoImage(Image.open(r"D:\Python_Programs\projectRPSgame\scissorL2.png"))
scissor2 = ImageTk.PhotoImage(Image.open(r"D:\Python_Programs\projectRPSgame\scissorR2.png"))

head = Label(root,font=("helvetica",30,"bold"),text="Rock Paper Scissor Game",bg="#fff6b0",fg="black").grid(row=1,column=2)
leave = Label(root,font=("helvetica",30,"bold"),text="-----------------------------------------",bg="#fff6b0",fg="black").grid(row=2,column=2)

#Labels for User and Computer scores
user_i = Label(root,font=("helvetica",30),text="User",bg="light blue",fg="black").grid(row=3,column=1)
computer_i = Label(root,font=("helvetica",30),text="Computer",bg="light blue",fg="black").grid(row=3,column=3)

#Initial images for both the players
player1 = Label(root, image=rock1, width=200, height=200)
player2 = Label(root, image=rock2, width=200, height=200)
player1.grid(row=5, column=0)
player2.grid(row=5, column=4)

#Scores of both the players
user_score = Label(root,text=0,font=("helvetica",60,"bold"),fg="black")
computer_score = Label(root,text=0,font=("helvetica",60,"bold"),fg="black")
user_score.grid(row=5,column=1)
computer_score.grid(row=5,column=3)

#Buttons to choose ROCK, PAPER or SCISSOR by the user
b_rock = Button(root,width=16,height=3,text="Rock",font=("arial",15,"bold"),bg="light blue",fg="black",command=lambda:update_choice("rock")).grid(row=6,column=1)
b_paper = Button(root,width=16,height=3,text="Paper",font=("arial",15,"bold"),bg="light blue",fg="black",command=lambda:update_choice("paper")).grid(row=6,column=2)
b_scissor = Button(root,width=16,height=3,text="Scissor",font=("arial",15,"bold"),bg="light blue",fg="black",command=lambda:update_choice("scissor")).grid(row=6,column=3)

def message(a):
    result['text'] = a

def point_comp():
    final = int(computer_score['text'])
    final += 1
    computer_score['text'] = str(final)

def point_user():
    final = int(user_score['text'])
    final += 1
    user_score['text'] = str(final)


def actual_game(u,c):
    if u == c:
        message("It is a tie!!!")
    elif u == "rock":
        if c == "paper":
            message("Computer Wins!! Better luck next time.") 
            point_comp()
        else:
            message("Hurray...You win!!!!") 
            point_user()
    elif u == "paper":
        if c == "scissor":
            message("Computer Wins!! Better luck next time.") 
            point_comp()
        else:
            message("Hurray...You win!!!!") 
            point_user()
    elif u == "scissor":
        if c == "rock":
            message("Computer Wins!! Better luck next time.") 
            point_comp()
        else:
            message("Hurray...You win!!!!") 
            point_user()

choices = ["rock","paper","scissor"]
def update_choice(a):
    choice_comp = choices[randint(0,2)]
    if choice_comp == "rock":
        player2.configure(image=rock2)
    elif choice_comp == "paper":
        player2.configure(image=paper2)
    else:
        player2.configure(image=scissor2)

    if a == "rock":
        player1.configure(image=rock1)
    elif a == "paper":
        player1.configure(image=paper1)
    else:
        player1.configure(image=scissor1)
        
    actual_game(a,choice_comp)

result =  Label(root,font=("helvetica",30,"bold"),bg="#fff6b0",fg="black")
result.grid(row=7,column=2)


root.mainloop()