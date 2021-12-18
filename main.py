import tkinter as tk
from tkinter import filedialog as fd, ttk
from openpyxl import Workbook, load_workbook


def callback(*args):
    """Функция вызываеься когда изменяется переменная file_path"""
    """Отслеживаем тем самым ее изменение"""
    print("Ye")
    print(args)


def choose_file():
    """Функция обработки нажатия кнопки и выбора файла"""
    filetypes = (("Таблица EXCEL", "*.xlsx"),
                 ("Любой", "*"))
    choose_file_path = fd.askopenfilename(title="Открыть файл", initialdir="/home",
                                          filetypes=filetypes)
    if not file_path:
        return
    else:
        print(file_path)
        label1["text"] = "Файл загружен"
        file_path.set(choose_file_path)
        print(file_path.get())


def tf(value):
    print(value)


def check():
    pass


root = tk.Tk()
root.geometry("300x400")

main_menu = tk.Menu(root)
root.config(menu=main_menu)


file_menu = tk.Menu(main_menu, tearoff=0)
settings_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
settings_menu.add_command(label="Settings")
settings_menu.add_command(label="Data base")


main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Settings", menu=settings_menu)

file_path = tk.StringVar()

label1 = tk.Label(text="Привет")
open_button = ttk.Button(root, text='OPEN FILE', command=choose_file)
btn_1= ttk.Button(root, text='Кнопка 1', command=lambda: tf(7))
btn_2= ttk.Button(root, text='Кнопка 1', command=lambda: print(8))
label1.pack()
open_button.pack()
btn_1.pack()
btn_2.pack()

file_path.trace('w', callback)

root.mainloop()
