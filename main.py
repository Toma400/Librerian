import path_mg as p; p.initialise_path()
from core.elements.account import Account
from core.technical import log_manag as log_manag
from core.gui import menu as menu
from core.gui import window as window
import logging as log
import traceback

log_manag.run()
try:
    win = window.runWindow(); log.info("Window succesfully initialised!"); win.read()
    acc: Account = menu.runAccount(win)
    menu.runMain(acc, win)
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