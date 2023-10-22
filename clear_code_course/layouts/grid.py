import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Grid")
window.geometry("600x400")

# widgets
label1 = ttk.Label(window, text="Label1", background="red")
label2 = ttk.Label(window, text="Label2", background="blue")
label3 = ttk.Label(window, text="Label3", background="yellow")
label4 = ttk.Label(window, text="Label4", background="green")
button1 = ttk.Button(window, text = "Button 1")
button2 = ttk.Button(window, text = "Button 2")
entry = ttk.Entry(window)

# define a grid
window.columnconfigure((0,1,2), weight = 1, uniform = "a")
window.columnconfigure(3, weight = 2, uniform = "a")
window.rowconfigure(0, weight = 1, uniform = "a")
window.rowconfigure(1, weight = 1, uniform = "a")
window.rowconfigure(2, weight = 1, uniform = "a")
window.rowconfigure(3, weight = 3, uniform = "a")

# place a widget
label1.grid(row = 0, column = 0, sticky = "nsew")
label2.grid(row = 1, column = 1, rowspan = 3, sticky = "nsew")
label3.grid(row = 1, column = 0, columnspan = 3, sticky = "nsew")
label4.grid(row = 3, column = 3, columnspan = 3, sticky = "se")

# exercise
# add the button and the entry field
button1.grid(row = 0, column = 3, sticky = "nesw")
button2.grid(row = 2, column = 2, sticky = "nsew")
entry.grid(row = 2, column = 3, rowspan = 2, sticky = "nsew")

# run
window.mainloop()
