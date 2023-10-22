import tkinter as tk
from tkinter import ttk

def button_function():
    print("A button was pressed")

def exercise_function():
    print("hello")
        
# create a window
window = tk.Tk()
window.title("Window and widgets")
window.geometry("800x500")

# ttk label
label = ttk.Label(master = window, text = "This is a test")
label.pack()

# tk.text
text = tk.Text(master = window)
text.pack()

# ttk.entry
entry = ttk.Entry(master = window)
entry.pack()
###############EXERCISE###############
my_label = ttk.Label(master = window, text ="my label")
my_label.pack()
# my_button = ttk.Button(master = window, text = "my button", command = exercise_function)
my_button = ttk.Button(master = window, text = "my_button", command = lambda:print("Hello"))
my_button.pack()
######################################
# ttk.button
button = ttk.Button(master = window, text = "A button", command = button_function)
button.pack()

# exercise 
# add one more text label and a button with a function that prints 'hello'
# the label should say "my label" and be between the entry widget and the button

# run
window.mainloop()
