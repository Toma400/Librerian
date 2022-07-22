import path_mg as p; p.initialise_path()
from core.technical import log_manag as log_manag
from core.gui import menu as menu
import logging as log
import traceback

log_manag.run()

try:
    menu.runAccount()
except:
    print("---------------------------------------------------------")
    log.critical("Main chain stopped. Printing the issue.", exc_info=True)
    traceback.print_exc()
    print("\n---------------------------------------------------------")
    print("Found an error! See the message above for details")
    print("You can send message above to developer, reporting the issue")
    print("\nEnter any key to close the game")
    temp_var = input("")