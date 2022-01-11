from tkinter import *
from tkinter.messagebox import *
import sys


class Tips():
    def about(root):
        showinfo(title="Tips", message="Please install Python(Latest Version) properly before running a python file and if you come across any problems while running a python script please check your Python installation because our IDE runs files using  default terminal of your PC")


def main(root, text, menubar):

    tips = Tips()

    tipsMenu = Menu(menubar)
    tipsMenu.add_command(label="Tips", command=tips.about)
    menubar.add_cascade(label="Tips", menu=tipsMenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    print("Please run 'Urinia'")