from string import ascii_uppercase
from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Tebak nama kota Indo //Challenged by Jo")

word = ["SURABAYA","PALU","JAKARTA","BATU BARA","SIANTAR","MEDAN","PERBAUNGAN","BEKASI","BANDUNG","JOGJA","SOLO","PONTIANAK"]

photos = [PhotoImage(file = "hang0.png"),PhotoImage(file = "hang1.png"),PhotoImage(file = "hang2.png"),PhotoImage(file = "hang3.png")
          ,PhotoImage(file = "hang4.png"),PhotoImage(file = "hang5.png"),PhotoImage(file = "hang6.png"),
          PhotoImage(file = "hang7.png"),PhotoImage(file = "hang8.png"),PhotoImage(file = "hang9.png")]

def new():
    global the_word_withSpaces
    global guessed
    guessed = 0
    imgLabel.config(image = photos[0])
    the_word = random.choice(word)
    the_word_withSpaces =" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))

def guess(letter):
    global  guessed
    if guessed<11:
        txt = list(the_word_withSpaces)
        guess = list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guess[c] = letter
                lblWord.set("".join(guess))
                if lblWord.get() == the_word_withSpaces:
                    messagebox.showinfo("Hangman","You Winn")
        else:
            guessed+=1
            imgLabel.config(image = photos[guessed])
            if guessed == 11:
                messagebox.showwarning("Hangman","Loser")

imgLabel = Label(root)
imgLabel.grid(row = 0,column = 0,columnspan=3, padx = 10,pady = 40)
imgLabel.config(image=photos[0])

lblWord = StringVar()
Label(root, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0,column=3,columnspan=6,padx=10)

n = 0
for c in ascii_uppercase:
    Button(root, text=c, command=lambda c=c: guess(c), font=("Helvetica 18"), width=4).grid(row = 1+n//9,column = n%9)
    n+=1

new()
root.mainloop()