from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list=password_letters+password_symbols+password_numbers
    random.shuffle(password_list)

    password="".join(password_list)
    # password = ""
    # for char in password_list:
    # password += char

    password_input.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
 website=web_input.get()
 email=email_input.get()
 password=password_input.get()
 new_data={
     website:{
         "email":email,
         "password":password,
     }
 }
 if len(website) == 0 or len(password) == 0:
         messagebox.showinfo(title="Error", message="Password/Website not filled!")
 else:
  option = messagebox.askokcancel(title=website, message=f"Details Entered:\nEmail:{email}\nPassword:{password}\nOk to Save?")

  if option:
    try:
         with open("password_manager.json", "r") as file:  # Use 'a' to append to the file
            # file.write(f"{website} | {email} | {password}\n")
            data=json.load(file)#read,read old data
    except FileNotFoundError:
            data = {}  # Initialize an empty dictionary if file is not found
    except json.JSONDecodeError:
         data = {}  # Initialize if the file exists but is empty or has invalid JSON
    finally:
         data.update(new_data)  # Update the old data with new data

         with open("password_manager.json", "w") as file:
             json.dump(data, file, indent=4)  # Write updated data back to the file

         web_input.delete(0, END)
         password_input.delete(0, END)
         web_input.focus()
def search():
    website=web_input.get()
    try:
         with open("password_manager.json", "r") as file:
          data=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Website Saved")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details found for {website}")


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

# filler_label=Label()
# filler_label.grid(column=0,row=0)

canvas=Canvas(width=200,height=200)#used to remove the thin white border between window and canvas
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)#to get image at centre of screen,we put coordinates at half of the canvas length
canvas.grid(column=1,row=0)

web_label=Label(text='Website:')
web_label.grid(column=0,row=1)

email_label=Label(text='Email/Username:')
email_label.grid(column=0,row=2)

password_label=Label(text='Password:')
password_label.grid(column=0,row=3)

web_input=Entry(width=21)
web_input.grid(column=1,row=1,sticky="EW")
web_input.focus()#brings cursor to this input entry the minute we launch GUI

email_input=Entry(width=21)
email_input.grid(column=1,row=2,columnspan=2,sticky="EW")
email_input.insert(0,"singh.navya300@gmail.com")

password_input=Entry(width=21)
password_input.grid(column=1,row=3,sticky="EW")

password_button=Button(text="Generate Password",command=generate_password)
password_button.grid(column=2,row=3,sticky="EW")

search_button=Button(text="Search",command=search)
search_button.grid(column=2,row=1,sticky="EW")

add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2,sticky="EW")




window.mainloop()