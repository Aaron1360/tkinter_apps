import ttkbootstrap as ttk

# calculate results
def calc_result(event):
    try:
        price = float(priceEntry.get())
        pieces = float(piecesEntry.get())
        unit = round(price/pieces,2)
        retail = round(unit*suggested_percentage,2)
        utility = round(retail-unit,2)
        price_per_unit.set(f"${unit}")
        retail_price.set(f"${retail}")
        utility_u.set(f"${utility} c/u")
        
    except: pass
    
# window
window = ttk.Window(
    title="Calculadora GV",
    size=(600,300),
    themename="solar",
    resizable=(False,False),
    iconphoto="/home/remote/Documents/code/tkinter_apps/gv_apps/python_dark.png"
)

# variables
price_per_unit = ttk.DoubleVar()
retail_price = ttk.DoubleVar()
utility_u= ttk.DoubleVar()
suggested_percentage =  1.15

# widgets
hdr_txt = "Ingresa el precio y el numero de piezas."
hdr = ttk.Label(window, text=hdr_txt, anchor="center", bootstyle="primary")

priceLabel = ttk.Label(window, text="Precio:")
priceEntry = ttk.Entry(window, width=10)

piecesLabel = ttk.Label(window, text="No. de piezas:")
piecesEntry = ttk.Entry(window, width=10)

unitLabel = ttk.Label(window, text="Precio por\nunidad:")
unitRes = ttk.Label(window, textvariable=price_per_unit, bootstyle="light")

retailLabel = ttk.Label(window, text="Precio sugerido\n(+15%):")
retailRes = ttk.Label(window, textvariable=retail_price, bootstyle="light")

utilityLabel = ttk.Label(window, text="Utilidad:")
utilityRes = ttk.Label(window, textvariable=utility_u, bootstyle="light")

# grid
window.rowconfigure((0,1,2,3), weight=1)
window.columnconfigure((0,1,2,3), weight=1)

# place widgets
hdr.grid(row = 0, column = 0, columnspan=4, sticky = 'nsew', padx = 10, pady = 10)

priceLabel.grid(row = 1, column = 0, sticky = 'nsew', padx = 10, pady = 10)
priceEntry.grid(row = 1, column = 1, sticky = 'ew', padx = 10, pady = 10)

piecesLabel.grid(row = 1, column = 2, sticky = 'nsew', padx = 10, pady = 10)
piecesEntry.grid(row = 1, column = 3, sticky = 'ew', padx = 10, pady = 10)

unitLabel.grid(row = 2, column = 0, sticky = 'nsew', padx = 10, pady = 10)
unitRes.grid(row = 2, column = 1, sticky = 'nsew', padx = 10, pady = 10)

retailLabel.grid(row = 2, column = 2, sticky = 'nsew', padx = 10, pady = 10)
retailRes.grid(row = 2, column = 3, sticky = 'nsew', padx = 10, pady = 10)

utilityLabel.grid(row = 3, column = 0, sticky = 'nsew', padx = 10, pady = 10)
utilityRes.grid(row = 3, column = 1, sticky = 'nsew', padx = 10, pady = 10)

# call the function
window.bind("<KeyPress-KP_Enter>", calc_result)

# run
window.mainloop()

