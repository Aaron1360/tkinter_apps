from tkinter import PhotoImage
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

app_icon = "to_do_list/icons/window.png"

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
        trash = PhotoImage(file="to_do_list/icons/trash-can.png")
        self.trash_icon=trash.subsample(23,23)
        
        self.main_frame = MainFrame(self)
        
        self.mainloop()
        
class MainFrame(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent,padding=10)
        self.pack(side=TOP,fill=BOTH,expand=TRUE)
        
        ttk.Label(master=self,name="title",text="Enter new task",anchor="center",font=("helvetica",14)).pack(side=TOP,fill=X)
        self.tasks_list = []
        self.addInputBar()
        self.addMenuFrame()
        self.addContentFrame()
        
    def addInputBar(self):
        inputFrame = ttk.Frame(master=self,padding=10)
        inputFrame.pack(side=TOP)
        self.text=ttk.StringVar()
        self.usrEntry = ttk.Entry(master=inputFrame,name="newTask",width=40,textvariable=self.text)
        self.usrEntry.pack(side=LEFT,anchor=N)
        inputFrame.nametowidget("newTask").focus_set()
        self.addBtn = ttk.Button(master=inputFrame,name="newTaskBtn",text="+",command=self.addNewTask)
        self.addBtn.pack(side=LEFT,anchor=N,padx=5)
        
    def addMenuFrame(self):
        MenuFrame = ttk.Frame(master=self,padding=10)
        MenuFrame.pack(side=TOP)
        
        buttons = ["All","Active","Completed"]
        
        for i, label in enumerate(buttons):
            ttk.Button(master=MenuFrame,name=label.lower(),text=label,padding=10).pack(side=LEFT,padx=10)
        
    def addContentFrame(self):
        self.contentFrame = ttk.Frame(master=self)
        self.contentFrame.pack(side=TOP,fill=BOTH)
        
        self.statusFrame = ttk.Frame(master=self.contentFrame)
        self.statusFrame.pack(side=BOTTOM,fill=X)
        
        self.count = ttk.IntVar(value=0)
        self.itemsLabel = ttk.Label(master=self.statusFrame,text=f"{self.count.get()} active item(s) left")
        self.itemsLabel.pack(side=LEFT,fill=X,expand=TRUE,anchor=E)
        clearButton = ttk.Button(master=self.statusFrame,text="Clear Completed",command=self.clearCompletedTasks)
        clearButton.pack(side=LEFT,fill=X)
        
    def updateLabel(self,operation):
        if operation == "add":
            self.count.set(self.count.get() + 1)
        elif operation == "sub":
            self.count.set(self.count.get() - 1)
        self.itemsLabel.config(text=f"{self.count.get()} active item(s) left")
    
    def addNewTask(self):
        if self.text.get()!="":
            newTask=Task(self.contentFrame,self.master,self.text.get())
            newTask.pack(side=TOP,anchor=NW,pady=3)
            self.tasks_list.append(newTask)
            self.updateLabel("add")
            
    def clearCompletedTasks(self):
        # 
        new_list=[]
        for t in self.tasks_list:
            if t.checkvar.get() == 1:
                t.deleteTask(update=FALSE)
                self.updateLabel("sub")
            else:
                new_list.append(t)
        self.tasks_list = new_list
        
    def testfunction(self):
        pass
    
class Task(ttk.Frame):
    def __init__(self,parent,mainWindow,task):
        super().__init__(parent)
        self.mainWindow=mainWindow
        self.checkvar = ttk.IntVar(value=0)
        ttk.Checkbutton(master=self,variable=self.checkvar).pack(side=LEFT)
        self.label=ttk.Label(master=self,text=task,width=40)
        self.label.pack(side=LEFT,fill=X,expand=TRUE)
        ttk.Button(master=self,image=self.mainWindow.trash_icon,style='Outline.TButton',command=lambda : self.deleteTask(update=TRUE)).pack(side=LEFT)

    def deleteTask(self,update):
        self.destroy()
        if update == TRUE:
            MainFrame.updateLabel(self.mainWindow.main_frame,"sub")
    
    def showText(self):

        print(self.label.cget("text"))

App("To-Do List","journal",(450,600)) 

# TODO: make another file and put the design in it, leave the functionality apart.
#       store the current notes and load them 
