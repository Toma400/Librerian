import os; fpath = os.path.dirname(os.path.abspath("main.py"))
import logging as log
###########################################################################
# ACCOUNT
###########################################################################
# Account class is used for creating and managing your users' data
#--------------------------------------------------------------------------

class Account:
    pass

def createAccount(name):
    import os
    try:
        log.info("Initialising account creation. Keep your fingers crossed!")
        os.mkdir(f"{fpath}/accounts/{name}/")
        log.info(f"Account {name} successfully created!")
        return True
    except FileExistsError:
        log.warning(f"Account with the name {name} exists!"); log.info("Refreshing the menu, please put different name")
        return False