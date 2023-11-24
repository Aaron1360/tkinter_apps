#!/usr/bin/env python
# FIFTH VERSION WITH AN EXTRA LABELFRAME
import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.constants import *

img = "prices_calculator/python.png" # <a href="https://www.flaticon.com/free-icons/python" title="python icons">Python icons created by Freepik - Flaticon</a>

# MAIN CLASS
class App(ttk.Window):
    def __init__(self,title,theme):
        
        # SETUP 
        super().__init__(
            title = title,
            themename = theme,
            iconphoto=img,
            minsize = (650,380),
            position = (400,200),
            resizable=(TRUE,TRUE))
        
        # ADD CONTENT 
        self.main_frame = MainFrame(self)
        
        # CALCULATE RESULT
        self.bind("<KeyPress-KP_Enter>", self.calcResult)
        self.bind("<KeyPress-Return>", self.calcResult)
        
        # RUN APP
        self.mainloop()

    def calcResult(self, event):
        try: # ids = ["percentage":0,"retail":1,"pieces":2,"utility":3,"unit":4,"price":5]
            price = float(self.main_frame.widgets[5].get())
            pieces = float(self.main_frame.widgets[2].get())
            unit = round(price/pieces,2)
            retail = round(unit*(1 + (self.main_frame.percentage.get() / 100)),2)
            utility = round(retail-unit,2)
            self.main_frame.widgets[4]["text"] = f"${unit}"
            self.main_frame.widgets[1]["text"] = f"${retail}"
            self.main_frame.widgets[3]["text"] = f"${utility} c/u"
        except:
            toast = ToastNotification(title="Error",message="Datos invalidos",duration=1000)
            toast.show_toast()
            
class MainFrame(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent,padding=10,style="dark")
        self.pack(fill = BOTH, expand = TRUE)
        self.percentage = ttk.IntVar(value = 15)
        
        # CREATE WIDGETS
        self.headerFrame()
        ttk.Separator(master = self, bootstyle = "light").pack(fill = X, pady = 10)
        self.widgets = self.calcFrames()

    def headerFrame(self):
        hdr_frame = ttk.Labelframe(
            master = self,
            text = "Instrucciones",
            bootstyle = "light",
            borderwidth = 10,
            relief="flat",
            labelanchor="n") # top frame
        
        hdr_txt = "Ingresa los datos del producto y presiona Intro/Enter para calcular el resultado."
        
        instruction_label = ttk.Label(
            master = hdr_frame,
            text = hdr_txt,
            bootstyle = "success",
            anchor = "center") # label with instructions
        
        instruction_label.pack(fill = X, expand = TRUE)
        hdr_frame.pack(fill = BOTH)
        
    def calcFrames(self):
        io_frame = ttk.Frame(master = self, borderwidth = 10, relief = "flat") # frame with data
        io_frame.rowconfigure((0,1,2), weight = 1, uniform = "a")
        io_frame.columnconfigure((0,1), weight = 1, uniform = "a")
        
        # FILL GRID WITH LABELFRAMES
        ids_list =["Precio:","Precio por unidad:","Utilidad:","No. de piezas:","Precio sugerido:","Porcentaje:"]
        for i,id in enumerate(ids_list):
            new_frame = ttk.Labelframe(master = io_frame, text = id, padding = 5)
            new_frame.grid(row=i if i<=2 else i-3, column= 0 if i<=2 else 1, sticky="nsew", padx=50, pady=10,)
        io_frame.pack(fill = BOTH, expand=TRUE)
        frames = io_frame.grid_slaves()# list of LabelFrames
        
        # ADD CONTENT OF EACH LABELFRAME 
        ttk.Entry(master = frames[5], name = "price", width = 10,style="light").pack(fill = X,expand = TRUE)
        ttk.Entry(master = frames[2], name = "pieces", width = 5,style="light").pack(fill = X,expand = TRUE)
        frames[5].nametowidget("price").focus_set()
        ttk.Label(master = frames[4], name = "unit",text="-", anchor="w", bootstyle="light").pack(fill = X,expand = TRUE)
        ttk.Label(master = frames[1], name = "retail",text="-", anchor="w", bootstyle="light").pack(fill = X,expand = TRUE)
        ttk.Label(master = frames[3], name = "utility",text="-", anchor="w", bootstyle="light").pack(fill = X,expand = TRUE)
        ttk.Spinbox(
            master = frames[0],
            name = "percentage",
            from_ = 0,
            to = 100,
            textvariable = self.percentage,
            bootstyle="light",).pack(fill = X,expand = TRUE)
        
        # RETURN LIST OF WIDGETS
        ids = ["percentage","retail","pieces","utility","unit","price"]
        widgets = []
        for i, id in enumerate(ids):
            widgets.append(frames[i].nametowidget(id))
        return widgets  
    
# CREATE INSTANCE OF THE APP
App("Calculadora de precios", "darkly")
