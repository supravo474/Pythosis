from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import *
from tkinter.scrolledtext import *
import file_menu
import edit_menu
import format_menu
import help_menu
import run_menu
import tips_menu
import terminal

root = Tk()

root.title("Pythosis")
root.geometry("300x250+300+300")
root.minsize(width=1400, height=750)



text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
text.pack(fill=Y, expand=1)
text.focus_set()


menubar = Menu(root)


file_menu.main(root, text, menubar)
edit_menu.main(root, text, menubar)
format_menu.main(root, text, menubar)
help_menu.main(root, text, menubar)
run_menu.main(root, text, menubar)
tips_menu.main(root, text, menubar)
terminal.main(root, text, menubar)


root.mainloop()