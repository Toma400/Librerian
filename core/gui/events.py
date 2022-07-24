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
    # Event finishing the program                                        |
    # -------------------------------------------------------------------|
    if event == gui.WINDOW_CLOSED or event == ":Exit":
        win.close()
    else:
        return win, event, values