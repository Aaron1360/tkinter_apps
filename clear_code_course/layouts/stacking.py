from smtplib import bCRLF
import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Stacking order")
window.geometry("400x600")

# widgets
label1 = ttk.Label(window, text = "Label 1", background = "green")
label2 = ttk.Label(window, text = "Label 2", background = "red")
label3 = ttk.Label(window, text = "Label 3", background = "blue")

# label1.lift()
# label2.lower()

button1 = tk.Button(window, text = "raise label 1", command = lambda: label1.lift(aboveThis= label2))
button2 = tk.Button(window, text = "raise label 2", command = lambda: label2.tkraise())
button3 = tk.Button(window, text = "raise label 3", command = lambda: label3.tkraise())

# layout
label1.place(x = 50, y = 100, width = 200, height = 120)
label2.place(x = 150, y = 60, width = 140, height = 100)
label3.place(x = 20, y = 89, width = 160, height = 90)

button1.place(rely = 1, relx = 0.7, anchor = "se")
button2.place(rely = 1, relx = 1, anchor = "se")
button3.place(rely = 1, relx = 0.6, anchor = "se")

# exercise
# add a third label and button

# run
window.mainloop()
