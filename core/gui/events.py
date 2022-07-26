from core.gui.layouts import menu_layout, login_layout
from core.elements import account as acc
from core.gui import window as window
from PySimpleGUI import Window
import PySimpleGUI as gui
import logging as log

def eventReader(win: Window, event: str, values, accname=""):
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
        acname = values[":NewAccountName"]; result = acc.createAccount(acname)
        if result: win.close(); win = window.runFWindow(login_layout())
    # -------------------------------------------------------------------|
    # Event passing account name to further use; operated on main.py     |
    # module actually                                                    |
    # -------------------------------------------------------------------|
    elif event == ":EnterAccount":
        acname = values[":AccountsListed"]
        try:
            log.info(f"Attempted to log into account: {acname[0]}")
            win.close(); win = window.runFWindow(menu_layout())
        except IndexError: log.debug("No accounts selected or made, login attempt failed.")
    # -------------|------------------------------------------------------|
    # MENU         |                                                      |
    # SECTION      |                                                      |
    # -------------|------------------------------------------------------|
    elif event == ":Donate":
        import webbrowser; url = "https://www.patreon.com/Toma400/"
        webbrowser.open(url, new=0, autoraise=True)
    # -------------------------------------------------------------------|
    # Event finishing the program                                        |
    # -------------------------------------------------------------------|
    if event == gui.WINDOW_CLOSED or event == ":Exit":
        win.close()
    else:
        return win