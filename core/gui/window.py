from core.technical.repo_manag import tomlm as t; settings = t("settings.toml"); s = settings["General"]; winset = s["window"]
from core.technical.repo_manag import tomlm as t; m = t("init.toml")
from core.technical.repo_manag import screen_change
import core.gui.layouts as layouts
import logging as log
import PySimpleGUI as gui
import importlib
import copy

#--------------|----------------------------------
# THEME        |
#--------------|----------------------------------
mn_text = layouts.mn_text
mn_back = layouts.mn_back
mn_butt = layouts.mn_butt
ls_scrl = layouts.ls_scrl

#--------------|---------------------------------------|------------|-----------------------------------------------------
# WINDOW       | Used to create a window with          | KEYS:  idf > identificator, used for recognising window we enter
# RUNNERS      | specific layout                       |        val > values which needs to be returned through
#--------------|---------------------------------------|------------|-----------------------------------------------------
#| For simple layout variable
def runWindow(layout: str, init=False):
    log.info("Initialising the program window...") if init else log.info(f"Jumping into window >{layout}<")
    flayout = copy.deepcopy(getattr(layouts, layout)) # deepcopy helps avoiding reuse of the same layout object
    window = makeWindow(flayout)
    return window

#| For layout function (used if you need to input some mutable elements)
def runFWindow(layout, idf: str, init=False):
    log.info("Initialising the program window...") if init else log.info(f"Jumping into functional window >{idf}<")
    # ^ https://stackoverflow.com/questions/218616/how-to-get-method-parameter-names <- for {layout} (also func.__name__)
    flayout = copy.deepcopy(layout)
    window = makeWindow(flayout)
    return window

#| For layout which needs to return values
def runAdvWindow(layout, idf: str, init=False, *val):
    window = runFWindow(layout=layout, idf=idf, init=init)
    return window, *val

#--------------|----------------------------------
# OTHER        |
# UTILS        |
#--------------|----------------------------------
def makeWindow(flayout): #| window initialiser
    window = gui.Window(title=m["name"], layout=flayout, margins=(700, 500),                         #| general
                        resizable=True, no_titlebar=not winSet(), keep_on_top=winSet(),              #| objects
                        background_color=mn_back, button_color=mn_butt,                              #| colours
                        sbar_background_color=ls_scrl, sbar_arrow_color=mn_text, finalize=True)      #|
    # ^ stuff to add: resizable=True, maximized=dependent on settings
    if winSet(): window.maximize()
    return window

def winSet():
    setv = winset.capitalize()
    if setv == "Fullscreen": return True
    elif setv == "Small": return False
    else:
        log.info(f"Incorrect settings found. Found Window setting is set to {setv}. Switching to default setting...")
        screen_change("Small")
        return False