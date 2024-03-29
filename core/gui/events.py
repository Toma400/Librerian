from core.gui.layouts import menu_layout, login_layout, settings_layout, setchange_layout, entrylist_layout, entryadd_layout
from core.technical.repo_manag import lang_change, theme_change, log_change, reverseeng_lang, logs_deleting, file_lister
import core.gui.layouts as layouts; import importlib
from core.elements import account as acc
from core.gui import window as window
from PySimpleGUI import Window
import PySimpleGUI as gui
import logging as log

from core.elements.blank_entry import Entry
imods = file_lister(f"entries/", ext="py") #| imports all modules from /entries/ folder
for x in imods:
    x1 = x.replace("\\", "."); x2 = x1.replace("\\", ".")
    __import__(x2)

def eventReader(win: Window, event: str, values, selentry: Entry.subclasses, accname=""):
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
    elif event == ":RejectAccountCreation":
        win.close(); win = window.runFWindow(login_layout(), idf="Login")
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
    #| Log-related events
    elif event == ":LogsSet":
        win.close(); win = window.runWindow("setlog_layout")
    elif event == ":SetchangeConfirmLogs":
        if values[":LogsSetNumber"]:
            loglim = values[":LogsSetNumber"]
            log_change(loglim)
        importlib.reload(layouts); importlib.reload(window) #| used to make changes appear
        win.close(); win = window.runFWindow(settings_layout(), idf="Settings")
    elif event == ":LogsRemove":
        logs_deleting()
    #|--------------------------
    #| Coming back to menu
    elif event == ":BackToMenu":
        win.close(); win = window.runFWindow(menu_layout(), idf="Menu")
    # -------------|------------------------------------------------------|
    # ENTRY        |                                                      |
    # SECTION      |                                                      |
    # -------------|------------------------------------------------------|
    elif event is not None and event.__contains__("EntryButton"):
        scrap = event.replace("EntryButton", ""); scrap = scrap.replace(":", "")
        for i in Entry.subclasses:
            if i.folder_key == scrap:
                selentry = i
        win.close(); win = window.runFWindow(entrylist_layout(accname, selentry), idf=f"Entry List: [{selentry.folder_key}]")
    elif event == ":EntryNew":
        win.close(); win = window.runFWindow(entryadd_layout(accname, selentry), idf=f"Adding New Item for Entry: [{selentry.folder_key}]")
    # -------------|------------------------------------------------------|
    # UPDATERS     |                                                      |
    # SECTION      |                                                      |
    # -------------|------------------------------------------------------|
    # Special function to handle events not doing any real change, but    |
    # update status or return some valuable information                   |
    # --------------------------------------------------------------------|
    entrylist_updater = [":EntryItemsId", ":EntryItemsData"]
    # V^ does not work anyway, lol
    if event is not None and event in entrylist_updater:
        print("!!!!!!!!!!!!!!!!!!!")
        selects = win[event].get_indexes()
        if not selects:
            pass
        else:
            for key in entrylist_updater:
                win[key].update(set_to_index=selects)
        win.refresh()
        win[":EntryColumn"].contents_changed()

    # -------------------------------------------------------------------|
    # Event finishing the program                                        |
    # -------------------------------------------------------------------|
    if event == gui.WINDOW_CLOSED or event == ":Exit":
        win.close()
    else:
        return win