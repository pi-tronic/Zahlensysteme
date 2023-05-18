from tkinter import Tk, Canvas, ttk

width = 420
height = 200

window = Tk()
window.title("Zahlensysteme GUI 3")
window.geometry(str(width)+"x"+str(height))

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
topleft = Canvas(window, width=width/2, height=height/3)
topleft.grid(column=0, row=0, sticky='nswe')

topright = Canvas(window, width=width/2, height=height/3)
topright.grid(column=1, row=0, sticky='nswe')

midleft = Canvas(window, width=width/2, height=height/3)
midleft.grid(column=0, row=1, sticky='nswe')

midright = Canvas(window, width=width/2, height=height/3)
midright.grid(column=1, row=1, sticky='nswe')

bottomleft = Canvas(window, width=width/2, height=height/3)
bottomleft.grid(column=0, row=3, sticky='nswe')

bottomright = Canvas(window, width=width/2, height=height/3)
bottomright.grid(column=1, row=3, sticky='nswe')

topleft.grid_columnconfigure(0, minsize=50, weight=1)
topright.grid_columnconfigure(0, minsize=50, weight=1)
midleft.grid_columnconfigure(0, minsize=50, weight=1)
midright.grid_columnconfigure(0, minsize=50, weight=1)
bottomleft.grid_rowconfigure(0, minsize=50, weight=1)
bottomleft.grid_columnconfigure(0, minsize=50, weight=1)
bottomright.grid_rowconfigure(0, minsize=50, weight=1)
bottomright.grid_columnconfigure(0, minsize=50, weight=1)


# create canvas for Entries
AEntry = Canvas(topleft, width=width/2, height=2*height/9)
AEntry.grid(column=0, row=1, sticky='nswe')

BEntry = Canvas(topright, width=width/2, height=2*height/9)
BEntry.grid(column=0, row=1, sticky='nswe')

IEntry = Canvas(midleft, width=width/2, height=2*height/9)
IEntry.grid(column=0, row=1, sticky='nswe')

OEntry = Canvas(midright, width=width/2, height=2*height/9)
OEntry.grid(column=0, row=1, sticky='nswe')

AEntry.grid_columnconfigure(0, minsize=50, weight=1)
BEntry.grid_columnconfigure(0, minsize=50, weight=1)
IEntry.grid_columnconfigure(0, minsize=50, weight=1)
OEntry.grid_columnconfigure(0, minsize=50, weight=1)


# create the text in every section
AText = ttk.Label(topleft, text="Alphabet A:", style="BW.TLabel")
AText.grid(column=0, row=0, padx=10, pady=10, sticky='w')

BText = ttk.Label(topright, text="Alphabet B:", style="BW.TLabel")
BText.grid(column=0, row=0, padx=10, pady=10, sticky='w')

IText = ttk.Label(midleft, text="Ausgangswert I:", style="BW.TLabel")
IText.grid(column=0, row=0, padx=10, pady=10, sticky='w')

OText = ttk.Label(midright, text="Ergebnis O:", style="BW.TLabel")
OText.grid(column=0, row=0, padx=10, pady=10, sticky='w')


# create the Entries
values = ["0,1",
          "0,1,2,3,4,5,6,7,8,9",
          "0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F"]

AEntry = ttk.Combobox(AEntry, width=19, values=values)
AEntry.grid(column=0, row=0, padx=10, pady=0, sticky='we')

BEntry = ttk.Combobox(BEntry, width=19, values=values)
BEntry.grid(column=0, row=0, padx=10, pady=0, sticky='we')

IEntry = ttk.Entry(IEntry, style="BW.TEntry")
IEntry.grid(column=0, row=0, padx=10, pady=0, sticky='we')

OEntry = ttk.Entry(OEntry, style="BW.TEntry")
OEntry.grid(column=0, row=0, padx=10, pady=0, sticky='we')


# define functions
def clearEntries():
    AEntry.delete(0,'end')
    BEntry.delete(0,'end')
    IEntry.delete(0,'end')
    OEntry.delete(0,'end')

def convert():
    OEntry.delete(0,'end')

    A = AEntry.get().split(',')
    B = BEntry.get().split(',')

    I = IEntry.get()

    ten = 0
    for i in range(len(I)):
        ten += A.index(I[i]) * len(A) ** (len(I)-1-i)

    V = []
    while ten!=0:
        mod = ten % len(B)
        V.insert(0, B[mod])

        ten = int(ten/len(B))

    O = ""
    for item in V:
        O += item
    OEntry.insert(0, O)


# create the Buttons
CButton = ttk.Button(bottomleft, text="Clear", command=clearEntries)
CButton.grid(column=0, row=0, padx=10, pady=10, sticky='nswe')

DButton = ttk.Button(bottomright, text="Convert", command=convert)
DButton.grid(column=0, row=0, padx=10, pady=10, sticky='nswe')


# mainloop
window.mainloop()
