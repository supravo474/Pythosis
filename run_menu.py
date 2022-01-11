from tkinter import *
from tkinter.messagebox import *
import sys
import os
from tkinter.filedialog import *


class Run():
    def cacsaeda(root):
        filename = askopenfilename()
        os.system("start cmd")
        os.system(filename)


def main(root, text, menubar):

    run = Run()

    runMenu = Menu(menubar)
    runMenu.add_command(label="Run", command=run.cacsaeda)
    menubar.add_cascade(label="Run", menu=runMenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    print("Please run 'Urinia'")