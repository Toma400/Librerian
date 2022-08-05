import os; os.chdir(os.path.dirname(os.path.abspath("main.py"))); import path_mg as p; p.initialise_path() #| system imports
from core.technical.repo_manag import tomlm as t; settings = t("settings.toml"); s = settings["General"]; lang = s["language"]; lnum = s["log_limit"]
from core.technical import log_manag as log_manag; log_manag.run()
from core.technical.repo_manag import reverseeng_warn
from core.technical.repo_manag import cache_deleting
from core.technical.repo_manag import logs_deleting
from core.technical.repo_manag import file_lister
from core.elements.blank_entry import Entry
from core.gui.layouts import login_layout
from core.gui import window as window
from core.gui import events as events
import PySimpleGUI as gui
import logging as log
import traceback

logs_deleting(lnum)
log.debug(p.path_info())
reverseeng_warn("current__language")
#----ENTRIES IMPORT---------------------------|---------------------------------------------------------------
for x in file_lister(f"entries/", ext="py"): #| imports all modules from /entries/ folder
    x1 = x.replace("\\", "."); x2 = x1.replace("\\", "."); log.debug(f"Module is being imported: [{x2}]")
    __import__(x2)

try:
    win = window.runFWindow(login_layout(), idf="Init", init=True); log.info("Window succesfully initialised!")
    accname  = ""   #| value before logging (overwritten by :EnterAccount event)
    selentry = None #| value before entering the entry (overwritten by :{i}EntryButton event)
    while True:
        event, values = win.read()
        win.refresh()
        win = events.eventReader(win, event, values, selentry, accname=accname)

        if event == ":EnterAccount":
            try: accname = (values[":AccountsListed"])[0]
            except IndexError: pass

        if event is not None and event.__contains__("EntryButton"):
            scrap = event.replace("EntryButton", ""); scrap = scrap.replace(":", "")
            for i in Entry.subclasses:
                if i.folder_key == scrap:
                    selentry = i

        if event == gui.WINDOW_CLOSED or event == ":Exit":
            break

    cache_deleting()

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
    print("\nEnter any key to close the program")
    temp_var = input("")