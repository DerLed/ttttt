import tkinter as tk
import tkinter.messagebox as mb
from tkinter import filedialog as fd, ttk
from openpyxl import Workbook, load_workbook


def callback(*args):
    """Функция вызываеься когда изменяется переменная file_path"""
    """Отслеживаем тем самым ее изменение"""
    print("Ye")
    print(args)


# def choose_file():
#     """Функция обработки нажатия кнопки и выбора файла"""
#     filetypes = (("Таблица EXCEL", "*.xlsx"),
#                  ("Любой", "*"))
#     choose_file_path = fd.askopenfilename(title="Открыть файл", initialdir="/home",
#                                           filetypes=filetypes)
#     if not file_path:
#         return
#     else:
#         print(file_path)
#         label1["text"] = "Файл загружен"
#         file_path.set(choose_file_path)
#         print(file_path.get())


# def create_settings_window():
#     settings_root = tk.Toplevel(root)
#     settings_root.grab_set()


def tf(value):
    print(value)


def check():
    pass


class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.protocol("WM_DELETE_WINDOW", self.confirm_delete)
        self.label = tk.Label(self, text="Это всплывающее окно")
        self.button = tk.Button(self, text="Закрыть", command=self.destroy)
        self.label.pack(padx=20, pady=20)
        self.button.pack(pady=5, ipadx=2, ipady=2)

    def confirm_delete(self):
        message = "Вы уверены, что хотите закрыть это окно?"
        if mb.askyesno(message=message, parent=self):
            self.destroy()


class App(tk.Tk):
    def __init__(self, height=300, weight=400):
        super().__init__()
        self.geometry(f"{height}x{weight}")
        main_menu = tk.Menu(self)
        file_menu = tk.Menu(main_menu, tearoff=0)
        settings_menu = tk.Menu(main_menu, tearoff=0)

        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.destroy)

        settings_menu.add_command(label="Settings")
        settings_menu.add_command(label="Data base")

        main_menu.add_cascade(label="File", menu=file_menu)
        main_menu.add_cascade(label="Settings", menu=settings_menu)
        self.config(menu=main_menu)

    # def create_settings_window(self):
    #     settings_root = tk.Toplevel(self)
    #     settings_root.grab_set()

        # self.btn = tk.Button(self, text="Открыть новое окно",
        #                      command=self.open_about)
        # self.btn.pack(padx=50, pady=20)
        #
    # def open_about(self):
    #     window = Window(self)
    #     window.grab_set()


# root = tk.Tk()
# root.geometry("300x400")
#
# main_menu = tk.Menu(root)
# root.config(menu=main_menu)
#
#
# file_menu = tk.Menu(main_menu, tearoff=0)
# settings_menu = tk.Menu(main_menu, tearoff=0)
# file_menu.add_command(label="Open")
# file_menu.add_command(label="Save")
# file_menu.add_separator()
# file_menu.add_command(label="Exit")
# settings_menu.add_command(label="Settings")
# settings_menu.add_command(label="Data base", command=create_settings_window)
#
#
# main_menu.add_cascade(label="File", menu=file_menu)
# main_menu.add_cascade(label="Settings", menu=settings_menu)
#
# file_path = tk.StringVar()
#
# label1 = tk.Label(text="Привет")
# open_button = ttk.Button(root, text='OPEN FILE', command=choose_file)
# btn_1= ttk.Button(root, text='Кнопка 1', command=lambda: tf(7))
# btn_2= ttk.Button(root, text='Кнопка 1', command=lambda: print(8))
# label1.pack()
# open_button.pack()
# btn_1.pack()
# btn_2.pack()
#
# file_path.trace('w', callback)
#
# root.mainloop()


if __name__ == "__main__":
    app = App(height=500, weight=600)
    app.mainloop()
