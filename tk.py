# from tkinter import *
# root=Tk()
# root.title("Label Example")
# label=Label(root,text="Hello Akshma",font=("calibri",12,"bold"))
# label.pack()

# def say_hello():
#     print("Hello Arjoo")
# button=Button(root,text="Click me",command=say_hello)
# button.pack()
    
# root.mainloop()

# from tkinter import *

# root = Tk()
# canvas = Canvas(root, width=300, height=200, bg="lightyellow")
# canvas.pack()

# # draw shapes
# canvas.create_line(45, 100, 200, 100, fill="red", width=3)
# canvas.create_rectangle(50, 50, 150, 120, fill="lightblue")
# canvas.create_oval(100, 100, 180, 160, fill="pink")

# root.mainloop()

# from tkinter import *

# root = Tk()
# root.title("Image Example")

# img = PhotoImage(file="biryani.jpg")
# label = Label(root, image=img)
# label.pack()

# root.mainloop()

# from tkinter import *

# root = Tk()
# menu_bar = Menu(root)

# # File menu
# file_menu = Menu(menu_bar, tearoff=40)
# file_menu.add_command(label="New")
# file_menu.add_command(label="Exit", command=root.quit)
# menu_bar.add_cascade(label="File", menu=file_menu)

# root.config(menu=menu_bar)
# root.mainloop()

# from tkinter import *

# def on_click(event):
#     print("Mouse clicked at:", event.x, event.y)

# root = Tk()
# root.bind("<Button-1>", on_click)  # Left mouse click
# root.mainloop()

# from tkinter import *

# def key_pressed(event):
#     print("Key pressed:", event.char)

# root = Tk()
# root.bind("<Key>", key_pressed)
# root.mainloop()


# from tkinter import *

# root = Tk()
# label = Label(root, text="Hello Akshma", bg="yellow", fg="blue", font=("Arial", 14))
# label.pack(pady=10)

# def change_text():
#     label.config(text="Welcome to Tkinter!")  # change property using method

# button = Button(root, text="Change Text", command=change_text)
# button.pack()

# root.mainloop()
