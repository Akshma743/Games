from tkinter import *

root = Tk()
label = Label(root, text="Hello Akshma", bg="yellow", fg="blue", font=("Arial", 14))
label.pack(pady=10)

def change_text():
    label.config(text="Welcome to Tkinter!")  # change property using method

button = Button(root, text="Change Text", command=change_text)
button.pack()

root.mainloop()