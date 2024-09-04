from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
my_timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text,text="00:00")
    label1.config(text='Timer', font=("Arial", 40), foreground=fg, background=YELLOW)
    spacer_label.config(text="", width=5, bg=YELLOW)
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    reps+=1
    if reps==1 or reps==3 or reps==5 or reps==7:
             count_down(work_sec)
             label1.config(text="Work",foreground=GREEN)
    elif reps==2 or reps==4 or reps==6:
            count_down(short_break_sec)
            label1.config(text="Short\n Break",foreground=PINK)
    elif reps==8:
            count_down(long_break_sec)
            label1.config(text="Long \nBreak",foreground=RED)
            reps=0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
     global my_timer
     my_timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        for _ in range(1,9,2):
            marks=""
            marks+=check
            label2.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
fg=GREEN
check="✔"

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)#used to remove the thin white border between window and canvas
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)#to get image at centre of screen,we put coordinates at half of the canvas length
timer_text=canvas.create_text(100 ,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)

spacer_label = Label(text="", width=5,bg=YELLOW)
spacer_label.grid(column=0, row=0)

button1 = Button(text="start",command=start_timer)
button1.grid(column=0,row=2,padx=10,pady=10)

button2= Button(text="Reset",command=reset_timer)
button2.grid(column=2,row=2,padx=10,pady=10)

label1=Label(text='Timer', font=("Arial", 40),foreground=fg,background=YELLOW)
label1.grid(column=1,row=0,padx=10,pady=10)

label2=Label(font=("Arial",20),foreground=fg,background=YELLOW)
label2.grid(column=1,row=3,padx=10,pady=10)

window.mainloop()