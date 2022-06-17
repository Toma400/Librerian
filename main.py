from core.technical import log_manag as log_manag
from core.gui import menu as menu

log_manag.run()

try:
    menu.run()
except:
    pass

#from tkinter import *
#from tkinter import ttk
#root = Tk()
#ttk.Button(root, text="Hello World").grid()
#root.mainloop()