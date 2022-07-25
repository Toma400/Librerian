from core.elements import account as acc
from core.gui import window as window
from PySimpleGUI import Window
import PySimpleGUI as gui
import logging as log
import os

def eventReader(win: Window, event: str, values):
    #-------------|------------------------------------------------------|
    # LOGGING     | win.run() and win.refresh() are ommited because they |
    # SECTION     | are predefined in main.py loop                       |
    #-------------|------------------------------------------------------|
    # Event passed when you switch menus to the adding account menu      |
    #--------------------------------------------------------------------|
    if event == ":AddAccount":
        win.close(); win = window.runWindow("logadd_layout")
    # -------------------------------------------------------------------|
    # Event confirming creation of an account, checking if there's any   |
    # possible error with the new account or not                         |
    # -------------------------------------------------------------------|
    elif event == ":ConfirmAccountCreation":
        accname = values[":NewAccountName"]; result = acc.createAccount(accname)
        if result: win.close(); win = window.runWindow("login_layout"); log.info("Window successfully reinitialised!")
    # -------------------------------------------------------------------|
    # Event passing account name to further use; operated on main.py     |
    # module actually                                                    |
    # -------------------------------------------------------------------|
    elif event == ":EnterAccount":
        accname = values[":AccountsListed"]
        try:
            log.info(f"Attempted to log into account: {accname[0]}")
            win.close() # temporary closing
        except IndexError: log.debug("No accounts selected or made, login attempt failed.")
    # -------------------------------------------------------------------|
    # Event finishing the program                                        |
    # -------------------------------------------------------------------|
    if event == gui.WINDOW_CLOSED or event == ":Exit":
        win.close()
    else:
        return win