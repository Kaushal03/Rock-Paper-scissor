from tkinter import *
import time
import random
import os
from tkinter import messagebox as mb





rt=Tk()
rt.geometry("1600x800+0+0") 
rt.title("ROCK PAPER SCISSOR")
#####################################################################################
Tops=Frame(rt,width = 1600,height = 50,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(rt,width = 550,height = 700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(rt,width = 300,height = 700,relief=SUNKEN)
f2.pack(side=RIGHT)
########################################################################################################################
lblInfo=Label(Tops,font=("arial",30,"bold"),text="WELCOME TO THE GAME ROCK PAPER SCISSOR",fg="Steel Blue",bd=10,anchor="w")
lblInfo.pack()

localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

lblDateTime=Label(Tops,font=("arial",20,"bold"),text=localtime,fg="Steel Blue",bd=10,anchor="w")
lblDateTime.pack()

lblInfo=Label(Tops,font=("arial",23,"bold"),text=" ",fg="Steel Blue",bd=10,anchor="w")
lblInfo.pack()

lblInfo=Label(Tops,font=("arial",23,"bold"),text="PRESS START BUTTON TO START THE GAME ",fg="Steel Blue",bd=10,anchor="w")
lblInfo.pack()
#########################################################################################################################
def start():
    global game_window
    global player_score
    global computer_score
    global player_input
    global options
    global player_score_label
    global computer_input
    global player_options
    global winner_label
    global game_title
    global player_choice_label
    global computer_score_label
    global computer_choice_label
    global input_frame
    game_window=Toplevel(rt)
    game_window.title("Rock Paper Scissors Game")
    player_score = 0
    computer_score = 0
    options = [('rock',0), ('paper',1), ('scissors',2)]

    def player_choice(player_input):
        global player_score, computer_score

        computer_input = get_computer_choice()

        player_choice_label.config(text = 'Your Selected : ' + player_input[0])
        computer_choice_label.config(text = 'Computer Selected : ' + computer_input[0])

        if(player_input == computer_input):
            winner_label.config(text = "Tie")

        elif((player_input[1] - computer_input[1]) % 3 == 1):
            player_score += 1
            winner_label.config(text="You Won!!!")
            player_score_label.config(text = 'Your Score : ' + str(player_score))
        else:
            computer_score += 1
            winner_label.config(text="Computer Won!!!")
            computer_score_label.config(text='Your Score : ' + str(computer_score))

    #Function to Randomly Select Computer Choice
    def get_computer_choice():
        return random.choice(options)
    ###################################

    app_font = font=(12)

    #Displaying Game Title

    #Label to dispay, who wins each time
    winner_label = Label(game_window,text = "", fg = 'green', font = (13), pady = 8)
    winner_label.pack()

    input_frame = Frame(game_window)
    input_frame.pack()

    #Displaying player options
    player_options = Label(input_frame, text = "Your Options : ", font = app_font, fg = 'grey')
    player_options.grid(row = 0, column = 0, pady = 8)

    rock_btn = Button(input_frame, text = 'Rock', width = 15, bd = 0, bg = 'pink', pady = 5, command = lambda: player_choice(options[0]))
    rock_btn.grid(row = 1, column = 1, padx = 8, pady = 5)

    paper_btn = Button(input_frame, text = 'Paper', width = 15, bd = 0, bg = 'silver', pady = 5, command = lambda: player_choice(options[1]))
    paper_btn.grid(row = 1, column = 2, padx = 8, pady = 5)

    scissors_btn = Button(input_frame, text = 'Scissors', width = 15, bd = 0, bg = 'light blue', pady = 5, command = lambda: player_choice(options[2]))
    scissors_btn.grid(row = 1, column = 3, padx = 8, pady = 5)

    #Displaying Score and players choise
    score_label = Label(input_frame, text = 'Score : ', font = app_font, fg = 'grey')
    score_label.grid(row = 2, column = 0)

    player_choice_label = Label(input_frame, text = 'Your Selected : ---', font = app_font)
    player_choice_label.grid(row = 3, column = 1, pady = 5)

    player_score_label = Label(input_frame, text = 'Your Score : -', font = app_font)
    player_score_label.grid(row = 3, column = 2, pady = 5)

    computer_choice_label = Label(input_frame, text = 'Computer Selected : ---', font = app_font, fg = 'black')
    computer_choice_label.grid(row = 4, column = 1, pady = 5)

    computer_score_label = Label(input_frame, text = 'Computer Score : -', font = app_font, fg = 'black')
    computer_score_label.grid(row = 4, column = 2, padx = (10,0), pady = 5)

    game_window.geometry('700x300')
    game_window.mainloop()



lblInfo=Label(Tops,font=("arial",23,"bold"),text=" ",fg="Steel Blue",bd=10,anchor="w")
lblInfo.pack()

btn15=Button(rt,padx=16,pady=16,bd=8,fg="black",font=("arial",18,"bold"),text="START",bg="powder blue",
                    command=start,anchor="w",width=10,height=0,compound="c")
btn15.place(x=220,y=420)
def call(): 
	res = mb.askquestion('Exit Application', 'Do you really want to exit') 
	
	if res == 'yes' : 
		rt.destroy() 
		
	else : 
		mb.showinfo('Return', 'Returning to main application') 



btn16=Button(rt,padx=16,pady=16,bd=8,fg="black",font=("arial",18,"bold"),text="Quit",bg="powder blue",
                    command=call,anchor="w",width=10,height=0,compound="c")
btn16.place(x=620,y=420)

rt.mainloop()
