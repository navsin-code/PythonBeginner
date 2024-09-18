from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
import pandas
import random

current_card={}
to_learn={}
try:
 data=pandas.read_csv("data/Words_to_learn.csv")
except FileNotFoundError:
 orignal_data=pandas.read_csv("data/german_cards - Sheet1.csv")
 to_learn=orignal_data.to_dict(orient="records")
else:
 to_learn = data.to_dict(orient="records")




def next_card():
 global current_card,flip_timer
 window.after_cancel(flip_timer)
 current_card=random.choice(to_learn)
 canvas.itemconfig(card_title,text="German",fill="black")
 canvas.itemconfig(card_word,text=current_card["German"],fill="black")
 canvas.itemconfig(card_background,image=front_card)
 flip_timer=window.after(3000, func=flip_card)
def flip_card():
 canvas.itemconfig(card_title,text="English",fill="white")
 canvas.itemconfig(card_word,text=current_card["English"],fill="white")
 canvas.itemconfig(card_background,image=back_card)
window=Tk()
window.title("de-en")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

def is_known():
 to_learn.remove(current_card)
 data=pandas.DataFrame(to_learn)
 data.to_csv("data/Words_to_learn.csv",index=False)
 next_card()

flip_timer=window.after(3000, func=flip_card)

canvas=Canvas(width=800,height=526)
front_card=PhotoImage(file="images/card_front.png")#inside folder so need to specify
back_card=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=front_card)#centre of canvas
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
card_title=canvas.create_text(400,150,text="German",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))
cross_image=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=cross_image,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)
tick_image=PhotoImage(file="images/right.png")
right_button=Button(image=tick_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

next_card()


window.mainloop()

