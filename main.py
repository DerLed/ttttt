import tkinter as tk
from tkinter import filedialog as fd, ttk
from openpyxl import Workbook, load_workbook


def callback(*args):
    print("Ye")
    print(args)

def check_file_path(event):
    print("p")


def choose_file():

    filetypes = (("Таблица EXCEL", "*.xlsx"),
                 ("Любой", "*"))
    file_path1 = fd.askopenfilename(title="Открыть файл", initialdir="/home",
                                  filetypes=filetypes)
    if not file_path:
        return
    else:
        print(file_path1)
        label1["text"] = "Файл загружен"
        file_path.set(file_path1)
        print(file_path.get())


root = tk.Tk()
root.geometry("300x400")
file_path = tk.StringVar()
label1 = tk.Label(text="Привет")
open_button = ttk.Button(root, text='OPEN FILE', command=choose_file)

open_button.pack()
label1.pack()

file_path.trace('w', callback)
root.mainloop()
