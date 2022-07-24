from core.technical.repo_manag import tomlm as t; m = t("init.toml")
import os; fpath = os.path.dirname(os.path.abspath("main.py")) + r"\core\icon.ico"
import core.gui.layouts as layouts
import logging as log
import PySimpleGUI as gui
import copy

#--------------|----------------------------------
# THEME        |
#--------------|----------------------------------
mn_text = layouts.mn_text
mn_back = layouts.mn_back
mn_butt = layouts.mn_butt
ls_scrl = layouts.ls_scrl

def runWindow(layout: str, init=False):
    log.info("Initialising the program window...") if init else log.info(f"Jumping into window >{layout}<")
    flayout = copy.deepcopy(getattr(layouts, layout)) # deepcopy helps avoiding reuse of the same layout object
    window = gui.Window(title=m["name"], layout=flayout, margins=(700, 500),
                        icon=fpath, background_color=mn_back, button_color=mn_butt,
                        sbar_background_color=ls_scrl, sbar_arrow_color=mn_text, finalize=True)
    return window