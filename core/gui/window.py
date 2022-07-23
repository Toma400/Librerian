from core.technical.repo_manag import tomlm as t; m = t("init.toml")
import core.gui.layouts as layouts
import logging as log
import PySimpleGUI as gui

#--------------|----------------------------------
# THEME        |
#--------------|----------------------------------
mn_text = layouts.mn_text
mn_back = layouts.mn_back
mn_butt = layouts.mn_butt
ls_scrl = layouts.ls_scrl

def runWindow(layout: str):
    log.info("Initialising window...")
    flayout = getattr(layouts, layout)
    window = gui.Window(title=m["name"], layout=flayout, margins=(700, 500), return_keyboard_events=True,
                        icon="/core/icon.ico", background_color=mn_back, button_color=mn_butt, # return+icon not work
                        sbar_background_color=ls_scrl, sbar_arrow_color=mn_text)
    return window