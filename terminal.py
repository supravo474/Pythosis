from tkinter import *
from tkinter.messagebox import *
import sys
import os
from tkinter.filedialog import *


class Terminal():
    def term(root):
        os.system("start cmd") 


def main(root, text, menubar):

    terminal = Terminal()

    terminal_menu = Menu(menubar)
    terminal_menu.add_command(label="Terminal", command=terminal.term)
    menubar.add_cascade(label="Terminal", menu=terminal_menu)

    root.config(menu=menubar)


if __name__ == "__main__":
    print("Please run 'Urinia'")
