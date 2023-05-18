from tkinter import Tk, Canvas, ttk

width = 420
height = 250

window = Tk()
window.title("Binär - Rechnen")
window.geometry(str(width)+"x"+str(height))


# style
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background='#00BFFF')
style.configure("BW.TEntry", foreground="black", background="white")
style.configure("BW.TButton", foreground="black", background="white")

window.grid_columnconfigure(0, minsize=50, weight=1)
window.grid_columnconfigure(1, minsize=50, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, minsize=50, weight=1)

window.tk_setPalette(background='#00BFFF')


# create canvas for every section
topleft = Canvas(window, width=width/2, height=height/4)
topleft.grid(column=0, row=0, sticky='nswe')

topleft2 = Canvas(window, width=width/2, height=height/4)
topleft2.grid(column=0, row=1, sticky='nswe')

topright = Canvas(window, width=width, height=height/4)
topright.grid(column=1, row=0, sticky='nswe')

midleft = Canvas(window, width=width, height=height/4)
midleft.grid(column=0, row=2, sticky='nswe')

bottomleft = Canvas(window, width=width/2, height=height/4)
bottomleft.grid(column=0, row=3, sticky='nswe')

bottomright = Canvas(window, width=width/2, height=height/4)
bottomright.grid(column=1, row=3, sticky='nswe')

topleft.grid_columnconfigure(0, minsize=50, weight=1)
topleft2.grid_columnconfigure(0, minsize=50, weight=1)
topright.grid_columnconfigure(0, minsize=50, weight=1)
midleft.grid_columnconfigure(0, minsize=50, weight=1)
bottomleft.grid_rowconfigure(0, minsize=50, weight=1)
bottomleft.grid_columnconfigure(0, minsize=50, weight=1)
bottomright.grid_rowconfigure(0, minsize=50, weight=1)
bottomright.grid_columnconfigure(0, minsize=50, weight=1)


# create canvas for Entries
ACanvas = Canvas(topleft, width=width/2, height=2*height/9)
ACanvas.grid(column=0, row=1, sticky='nswe')

BCanvas = Canvas(topleft2, width=width/2, height=2*height/9)
BCanvas.grid(column=0, row=1, sticky='nswe')

CCanvas = Canvas(topright, width=width/2, height=2*height/9)
CCanvas.grid(column=0, row=1, sticky='nswe')

OCanvas = Canvas(midleft, width=width/2, height=2*height/9)
OCanvas.grid(column=0, row=1, sticky='nswe')

ACanvas.grid_columnconfigure(0, minsize=50, weight=1)
BCanvas.grid_columnconfigure(0, minsize=50, weight=1)
CCanvas.grid_columnconfigure(0, minsize=50, weight=1)
OCanvas.grid_columnconfigure(0, minsize=50, weight=1)


# create the text in every section
AText = ttk.Label(topleft, text="Zahl A:", style="BW.TLabel")
AText.grid(column=0, row=0, padx=10, pady=10, sticky='w')

BText = ttk.Label(topleft2, text="Zahl B:", style="BW.TLabel")
BText.grid(column=0, row=0, padx=10, pady=10, sticky='w')

BText = ttk.Label(topright, text="Type:", style="BW.TLabel")
BText.grid(column=0, row=0, padx=10, pady=10, sticky='w')

OText = ttk.Label(midleft, text="Result:", style="BW.TLabel")
OText.grid(column=0, row=0, padx=10, pady=10, sticky='w')


# create the Entries
values = ["Add",
          "Substract",
          "Multiply",
          "Substract"]

AEntry = ttk.Entry(ACanvas, style="BW.TEntry")
AEntry.grid(column=0, row=0, padx=10, pady=0, sticky='we')

BEntry = ttk.Entry(BCanvas, style="BW.TEntry")
BEntry.grid(column=0, row=0, padx=10, pady=0, sticky='we')

CEntry = ttk.Combobox(CCanvas, width=19, values=values)
CEntry.grid(column=0, row=0, padx=10, pady=0, sticky='we')

OEntry = ttk.Entry(OCanvas, style="BW.TEntry")
OEntry.grid(column=0, row=0, padx=10, pady=0, sticky='we')


# define functions
def clearEntries():
    AEntry.delete(0,'end')
    BEntry.delete(0,'end')
    CEntry.delete(0,'end')
    OEntry.delete(0,'end')

def add():
    OEntry.delete(0, 'end')

    A = AEntry.get()
    B = BEntry.get()

    O = bin(A)+bin(B)

    print(O)


# create the Buttons
CButton = ttk.Button(bottomleft, text="Clear", command=clearEntries)
CButton.grid(column=0, row=0, padx=10, pady=10, sticky='nswe')

DButton = ttk.Button(bottomright, text="Convert", command=add)
DButton.grid(column=0, row=0, padx=10, pady=10, sticky='nswe')


# mainloop
window.mainloop()
