import path_mg as p; p.initialise_path()
from core.technical.repo_manag import tomlm as t; settings = t("settings.toml"); s = settings["General"]; lang = s["language"]
from core.technical import log_manag as log_manag; log_manag.run()
from core.gui.layouts import login_layout
from core.gui import window as window
from core.gui import events as events
import PySimpleGUI as gui
import logging as log
import traceback

log.debug(p.path_info())
try:
    win = window.runFWindow(login_layout(), idf="Init", init=True); log.info("Window succesfully initialised!")
    accname = "" #| value before logging (overwritten by :EnterAccount event)
    while True:
        event, values = win.read()
        win.refresh()
        win = events.eventReader(win, event, values, accname)
        if event == ":EnterAccount":
            try: accname = (values[":AccountsListed"])[0]
            except IndexError: pass
        if event == gui.WINDOW_CLOSED or event == ":Exit":
            break
except KeyboardInterrupt:
    pass
except:
    print("---------------------------------------------------------")
    log.critical("Main chain stopped. Printing the issue.", exc_info=True)
    traceback.print_exc()
    print("\n---------------------------------------------------------")
    print('''
    Found an error! See the message above for details. 
    You can send message above to developer, reporting the issue.
    
    If you would like to send the error, please also take a look at "/logs" folder.
    You can provide developer latest log file, with name using newest date.
    This will help recognising the issue a lot faster.
    ''')
    print("\nEnter any key to close the game")
    temp_var = input("")