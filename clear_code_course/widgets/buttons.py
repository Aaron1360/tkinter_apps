import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title("buttons")
window.geometry("600x400")

# button
def button_function():
    print("The button was pressed\n")
    # print(radio_var.get())
    

button_string = tk.StringVar(value = "A button with string var")
button = ttk.Button(window,
                    text = "A simple button",
                    command = button_function,
                    textvariable = button_string)
button.pack()

# checkbutton
#check_var = tk.IntVar(value = 10)
check_var1 = tk.BooleanVar(value = True)
check1 = ttk.Checkbutton(window,
                         text = "checkbox 1",
                         # command = lambda: print(check_var.get()),
                         command = lambda: print("Checkbox 1 is selected") if check_var1.get() == True else check_var1.set(False),
                         variable = check_var1
                         # onvalue = 10,
                         # offvalue = 5
                        )
check1.pack()

check2 = ttk.Checkbutton(window,
                         text = "checkbox 2",
                        #  command = lambda: check_var.set(5))
                        # command = lambda: check_var1.set(False),
                        command = lambda: print("Checkbox 2 is selected") if check_var1.get() == False else check_var1.set(True),
                        variable = check_var1,
                        onvalue = False,
                        offvalue = True
                        )
check2.pack()

# radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window,
                         text = "radiobutton 1",
                         value = 1,
                         command = lambda: print("Radio1 is selected")
                         # variable = radio_var,
                         # command = lambda: print(radio_var.get()))
                        )
radio1.pack()

radio2 = ttk.Radiobutton(window,
                        text = "radiobutton 2",
                        value = 0,
                        command = lambda: print("Radio2 is selected")
                        # variable = radio_var)
)
radio2.pack()

# create another checkbutton and 2 radiobuttons 
# radio button:
	# values for the buttons are A and B
	# ticking either prints the value of the checkbutton
	# ticking the radio button unchecks the checkbutton
# check button: 
	# ticking the checkbutton prints the value of the radio button value 
	# use tkinter var for Booleans! 

# EXERCISE ##################################

# function
def rad_func():
    print(check_value.get())
    check_value.set(False)
# data
check_value = tk.BooleanVar()
radio_value = tk.StringVar()

# widgets
radioA = ttk.Radiobutton(window,
                         text = "Radio A",
                         value = "A",
                         command = rad_func,
                         variable = radio_value
                         )
radioB = ttk.Radiobutton(window,
                         text = "Radio B",
                         value = "B",
                         command = rad_func,
                         variable = radio_value
                         )
check3 = ttk.Checkbutton(window,
                         text = "Check",
                         variable = check_value,
                         command = lambda: print(radio_value.get())
                         )
# layout
radioA.pack()
radioB.pack()
check3.pack()
# run 
window.mainloop()