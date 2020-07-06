import os
from tkinter import filedialog, Button, Tk
from shutil import copyfile

window = Tk()

def folder_open():
    folder = filedialog.askdirectory()
    global start_folder
    start_folder = os.path.abspath(folder)

def folder_destination():
    folder = filedialog.askdirectory()
    global destination_folder
    destination_folder = os.path.abspath(folder)

def txt_file():
    file = filedialog.askopenfilename()
    if file:
        path_file = os.path.abspath(file)
        with open(path_file) as f:
            global file_txt
            file_txt = (f.read().splitlines())


def run_trans():
    for num in file_txt:
        for file in os.listdir(start_folder):
            if file.endswith(num + ".CR2"):
                copyfile(start_folder + "\\" + file, destination_folder + "\\" + file)

button_folder_open = Button(window, text="Выбери папку с файлами", command=folder_open)
button_folder_open.grid(column=0, row=0, pady=20)

button_folder_destination = Button(window, text="Выбери папку в которую загрузить файлы", command=folder_destination)
button_folder_destination.grid(column=0, row=1, pady=20)

button_numbers = Button(window, text="Выбери файл тхт с номерами", command=txt_file)
button_numbers.grid(column=0, row=2, pady=20)

button_run = Button(window, text="Переместить", command=run_trans, font=16, background="#FAF",)
button_run.grid(column=0, row=3, pady=20)

window.mainloop()
