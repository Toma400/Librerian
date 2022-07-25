from core.technical.repo_manag import tomlm as t; settings = t("settings.toml"); s = settings["General"]; winset = s["window"]
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
    window = gui.Window(title=m["name"], layout=flayout, margins=(700, 500),                     #| general
                        resizable=True, no_titlebar=not winSet(), keep_on_top=winSet(),          #| objects
                        background_color=mn_back, button_color=mn_butt,                          #| colours
                        sbar_background_color=ls_scrl, sbar_arrow_color=mn_text, finalize=True)  #|
    #stuff to add: resizable=True, maximized=dependent on settings, icon=fpath/scaling? [float]
    if winSet(): window.maximize()
    return window

def winSet():
    setv = winset.capitalize()
    if setv == "Fullscreen": return True
    elif setv == "Small": return False
    else:
        log.info(f"Incorrect settings found. Found Window setting is set to {setv}. Switching to default setting...")
        return True # in the future you can make it override incorrect value in .toml file and write default