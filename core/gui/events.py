from core.gui.layouts import menu_layout, login_layout, settings_layout, setchange_layout
from core.technical.repo_manag import lang_change, theme_change, reverseeng_lang
import core.gui.layouts as layouts; import importlib
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
        if result: win.close(); win = window.runFWindow(login_layout(), idf="Login")
    # -------------------------------------------------------------------|
    # Event passing account name to further use; operated on main.py     |
    # module actually                                                    |
    # -------------------------------------------------------------------|
    elif event == ":EnterAccount":
        acname = values[":AccountsListed"]
        try:
            log.info(f"Attempted to log into account: {acname[0]}")
            win.close(); win = window.runFWindow(menu_layout(), idf="Menu")
        except IndexError: log.debug("No accounts selected or made, login attempt failed.")
    # -------------|------------------------------------------------------|
    # MENU         |                                                      |
    # SECTION      |                                                      |
    # -------------|------------------------------------------------------|
    elif event == ":Donate":
        import webbrowser; url = "https://www.patreon.com/Toma400/"
        webbrowser.open(url, new=0, autoraise=True)
    elif event == ":EnterSettings":
        win.close(); win = window.runFWindow(settings_layout(), idf="Settings")
    # -------------------------------------------------------------------|
    # Events passed after attempting to change specific settings         |
    # Allows choosing language or theme                                  |
    # -------------------------------------------------------------------|
    #| Make new selection window appear
    elif event == ":ChangeLang":
        win.close(); win = window.runFWindow(setchange_layout("lang"), idf="ChangeLang")
    elif event == ":ChangeTheme":
        win.close(); win = window.runFWindow(setchange_layout("theme"), idf="ChangeTheme")
    #|--------------------------
    #| Run after using lang button
    elif event == ":SetchangeConfirmLang":
        if values[":LangListed"]:
            temp = values[":LangListed"] #| translation
            lgname = reverseeng_lang(temp[0], "current__language") #| detranslation
            lang_change(lgname)
        importlib.reload(layouts) #| used to make changes appear
        win.close(); win = window.runFWindow(settings_layout(), idf="Settings")
    #| Run after using theme button
    elif event == ":SetchangeConfirmTheme":
        if values[":ThemeListed"]:
            thname = values[":ThemeListed"]
            theme_change(thname)
        importlib.reload(layouts); importlib.reload(window) #| used to make changes appear
        win.close(); win = window.runFWindow(settings_layout(), idf="Settings")
    #|--------------------------
    #| Coming back to menu
    elif event == ":BackToMenu":
        win.close(); win = window.runFWindow(menu_layout(), idf="Menu")
    # -------------------------------------------------------------------|
    # Event finishing the program                                        |
    # -------------------------------------------------------------------|
    if event == gui.WINDOW_CLOSED or event == ":Exit":
        win.close()
    else:
        return win