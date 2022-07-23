import path_mg as p; p.initialise_path()
from core.technical import log_manag as log_manag
from core.gui import window as window
import PySimpleGUI as gui
import logging as log
import traceback

log_manag.run()
log.debug(p.path_info())
try:
    win = window.runWindow("login_layout"); log.info("Window succesfully initialised!");
    event = win.read()
    while True:
        #acc: Account = menu.runAccount(win)
        #win = window.runWindow("logadd_layout"); log.info("Window succesfully initialised!"); win.read()
        if event == gui.WINDOW_CLOSED:
            break
    win.close()
except KeyboardInterrupt:
    pass
except:
    print("---------------------------------------------------------")
    log.critical("Main chain stopped. Printing the issue.", exc_info=True)
    traceback.print_exc()
    print("\n---------------------------------------------------------")
    print("Found an error! See the message above for details")
    print("You can send message above to developer, reporting the issue")
    print("\nEnter any key to close the game")
    temp_var = input("")