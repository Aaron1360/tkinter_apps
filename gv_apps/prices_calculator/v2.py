import ttkbootstrap as ttk

app_icon="/home/remote/Documents/code/tkinter_apps/gv_apps/prices_calculator/python_dark.png"

# main class
class App(ttk.Window):
    def __init__(self,title,theme, icon):
        # setup
        super().__init__(title=title, themename=theme, iconphoto=icon, size=(600,350), resizable=(False,False))
        # variables
        self.price_per_unit = ttk.StringVar(value="-")
        self.retail_price = ttk.StringVar(value="-")
        self.utility = ttk.StringVar(value="-")
        self.price_entry = ttk.StringVar()
        self.pieces_entry = ttk.StringVar()
        var_list = [self.price_per_unit, self.retail_price, self.utility]
        entries_list = [self.price_entry, self.pieces_entry]
        self.suggested_percentage =  1.15
        # add content
        self.header = Header(self)
        self.body = Body(self, var_list, entries_list)
        # call the function
        self.bind("<KeyPress-KP_Enter>", self.calc_result)
        # run
        self.mainloop()
        
    def calc_result(self, event):
        try:
            price = float(self.price_entry.get())
            pieces = float(self.pieces_entry.get())
            unit = round(price/pieces,2)
            retail = round(unit*self.suggested_percentage,2)
            utility = round(retail-unit,2)
            self.price_per_unit.set(f"${unit}")
            self.retail_price.set(f"${retail}")
            self.utility.set(f"${utility} c/u")
        except: pass
        
class Header(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both")
        hdr_txt = "Ingresa el precio y el numero de piezas."
        hdr = ttk.Label(self, text=hdr_txt, anchor="s", bootstyle="primary", font=("Britannic Bold",13))    
        hdr.pack(fill="both", expand=True, ipady=20)

class Body(ttk.Frame):
    def __init__(self, parent, list1, list2):
        super().__init__(parent)
        self.parent=parent
        self.pack(fill="both", expand=True)
        self.create_widgets(list1, list2)
    
    def create_widgets(self, list1, list2):
        # create layout
        self.rowconfigure((0,1,2), weight=1)
        self.columnconfigure((0,1,2,3), weight=1)
        # labels
        label_txt = ["Precio:","Precio por\nunidad:","Utilidad:","No. de piezas:","Precio sugerido\n(+15%):"]
        for i,txt in enumerate(label_txt):
            label = ttk.Label(master=self, text=txt,anchor="w")
            label.grid(row=i if i<=2 else i-3, column= 0 if i<=2 else 2, sticky="nsew", padx=35, pady=10)
            # entries
            if i==1 or i==3:
                entry = ttk.Entry(master=self, textvariable=list2[0] if i==1 else list2[1], width=10)
                entry.grid(row=0, column=i, sticky="ew", padx=10, pady=10)
            # results
            if i<=2:
                result = ttk.Label(master=self, textvariable=list1[i],bootstyle="light")
                result.grid(row = 1 if i!=2 else 2, column= 1 if i!=1 else 3, sticky="ew", padx=10, pady=10)
# create an instance of the app
App("Calculadora GV", "solar", app_icon)
