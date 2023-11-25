from tkinter import PhotoImage
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.icons import Icon

app_icon = "to_do_list/python-file.png"# https://www.flaticon.com/free-icons/python-file  icon created by The Chohans

class App(ttk.Window):
    def __init__(self,title,theme,size):
        super().__init__(
            title = title,
            themename = theme,
            iconphoto=app_icon,
            minsize = size,
            position = (500,150),
            resizable=(FALSE,FALSE)
        )
        
        self.main_frame = MainFrame(self)
        
        self.mainloop()
        
class MainFrame(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent,padding=10)
        self.pack(side=TOP,fill=BOTH,expand=TRUE)
        
        ttk.Label(master=self,name="title",text="Enter new task",anchor="center",font=("helvetica",14)).pack(side=TOP,fill=X)
        
        self.addInputBar()
        self.addMenuFrame()
        self.addContentFrame()
        
    def addInputBar(self):
        inputFrame = ttk.Frame(master=self,padding=10)
        inputFrame.pack(side=TOP)
        
        ttk.Entry(master=inputFrame,name="newTask",width=40).pack(side=LEFT,anchor=N)
        inputFrame.nametowidget("newTask").focus_set()
        ttk.Button(master=inputFrame,name="newTaskBtn",text="+").pack(side=LEFT,anchor=N)
        
    def addMenuFrame(self):
        MenuFrame = ttk.Frame(master=self,padding=10)
        MenuFrame.pack(side=TOP)
        
        buttons = ["All","Active","Completed"]
        
        for i, label in enumerate(buttons):
            ttk.Button(master=MenuFrame,name=label.lower(),text=label,padding=10).pack(side=LEFT,padx=10)
        
    def addContentFrame(self):
        contentFrame = ttk.Frame(master=self)
        contentFrame.pack(side=TOP,fill=BOTH)
        
        statusFrame = ttk.Frame(master=contentFrame)
        statusFrame.pack(side=BOTTOM,fill=X)
        
        itemsLabel = ttk.Label(master=statusFrame,text="active item(s) left")
        itemsLabel.pack(side=LEFT,fill=X,expand=TRUE,anchor=E)
        clearButton = ttk.Button(master=statusFrame,text="Clear Completed")
        clearButton.pack(side=LEFT,fill=X)
        
        newTask=Task(contentFrame,"some boring task")
        newTask.pack(side=TOP)
        
class Task(ttk.Frame):
    def __init__(self,parent,task):
        pencil_icon = PhotoImage(file="to_do_list/pencil.png") # https://www.flaticon.com/free-icons/pencil created by Mayor Icons
        trash_icon = "to_do_list/trash-can.png" # https://www.flaticon.com/free-icons/trash created by Freepik 
        super().__init__(parent)
        ttk.Checkbutton(master=self).pack(side=LEFT)
        ttk.Label(master=self,text=task).pack(side=LEFT,fill=X,expand=TRUE)
        ttk.Button(master=self,image=pencil_icon).pack(side=LEFT)
        ttk.Button(master=self).pack(side=LEFT)
        
App("To-Do List","journal",(450,600))
# help(ttk.Window) 
