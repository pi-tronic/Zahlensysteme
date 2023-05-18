from tkinter import ttk
import tkinter as tk

window = tk.Tk()
window.title("Zahlensysteme")
window.geometry("420x200")

style = ttk.Style()
style.configure("BW.TEntry", foreground="black", background="white")
style.configure("BW.TButton", foreground="black", background="white")


AText = ttk.Label(window, text="Alphabet A:")
AText.grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)
BText = ttk.Label(window, text="Alphabet B:")
BText.grid(column=1, row=0, padx=10, pady=10, sticky=tk.W)
IText = ttk.Label(window, text="Ausgangswert I:")
IText.grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)
OText = ttk.Label(window, text="Ergebnis O:")
OText.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)


AEntry = ttk.Entry(window, style="BW.TEntry")
AEntry.grid(column=0, row=1, padx=10, pady=0, sticky=tk.E)

BEntry = ttk.Entry(window, style="BW.TEntry")
BEntry.grid(column=1, row=1, padx=10, pady=0, sticky=tk.W)

IEntry = ttk.Entry(window, style="BW.TEntry")
IEntry.grid(column=0, row=3, padx=10, pady=0, sticky=tk.E)

OEntry = ttk.Entry(window, style="BW.TEntry")
OEntry.grid(column=1, row=3, padx=10, pady=0, sticky=tk.W)

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

CButton = ttk.Button(window, text="Clear", command=clearEntries)
CButton.grid(column=0, row=4, padx=10, pady=10)

DButton = ttk.Button(window, text="Convert", command=convert)
DButton.grid(column=1, row=4, padx=10, pady=10)

AEntry.focus()

window.mainloop()
