from core.technical.repo_manag import tomlm as t; titlebar = t(); titlebar = titlebar["Titlebar"]
from core.elements.account import Account
import logging as log
import path_mg as p

name = "Librerian"
colour_text = titlebar["text_colour"]
colour_back = titlebar["background_colour"]

def runAccount(window):
    log.debug(p.path_info())

def runMain(account: Account, window):
    pass