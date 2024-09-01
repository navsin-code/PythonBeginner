from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=200, height=200)

# Create a spacer label (empty) for spacing
spacer_label = Label(text="", width=5)
spacer_label.grid(column=1, row=0)

label1 = Label(text='is equal to', font=("Arial", 15))
label1.grid(column=0, row=2, padx=10, pady=10)

label2 = Label(text='Km', font=("Arial", 15))
label2.grid(column=2, row=2, padx=10, pady=10)

label3=Label(text='Miles', font=("Arial", 15))
label3.grid(column=2, row=0, padx=10, pady=10)

label4=Label(text="0",font=("Arial",15))
label4.grid(column=1, row=2, padx=10, pady=10)

input=Entry(width=10)
input.grid(column=1, row=0, padx=10, pady=10)

def output():
    miles= float(input.get())
    kilometer=round(miles*1.609344,4)
    label4.config(text=str(kilometer))
button = Button(text="Click me", command=output)
button.grid(column=1,row=3,padx=10,pady=10)
window.mainloop()








window.mainloop()