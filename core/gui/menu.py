import logging
from tkinter import *
from tkinter import ttk

name = "Librerian"
padding_values = "3 3 12 12"

def run():
    #---------------------------------------------------
    # SCREEN INITIALISATION
    #---------------------------------------------------
    logging.debug("Initialising Tkinter...")
    root = Tk()
    root.title(name)
    logging.debug("Tkinter initialised menu. Moving to values.")
    # ---------------------------------------------------
    # Height x Width values
    mainframe = ttk.Frame(root, padding=padding_values)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    logging.debug("Tkinter successfully initialised values.")
    # ---------------------------------------------------
    # Builders
    # ---------
    # Name input
    name_input = StringVar()
    name_entry = ttk.Entry(mainframe, textvariable=name_input)
    name_entry.grid(column=2, row=1, sticky=(W, E))
    logging.debug("Tkinter initialised name input value")
    # Name output
    name_confirmation = StringVar()
    ttk.Label(mainframe, textvariable=name_confirmation).grid(column=2, row=2, sticky=(W, E))
    logging.debug("Tkinter initialised name output value")
    # Buttons
    ttk.Button(mainframe, text="Enter").grid(column=3, row=3, sticky=W)
    ttk.Button(mainframe, text="Confirm").grid(column=2, row=3, sticky=W)
    # Labels
    ttk.Label(mainframe, text="| Enter profile name").grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text="| Confirm?").grid(column=3, row=2, sticky=W)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)
    name_entry.focus()
    root.bind("<Return>")