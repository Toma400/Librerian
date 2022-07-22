from core.technical.repo_manag import tomlm as t; titlebar = t(); titlebar = titlebar["Titlebar"]
import logging as log
import PySimpleGUI as gui
import path_mg as p

name = "Librerian"
colour_text = titlebar["text_colour"]
colour_back = titlebar["background_colour"]

def runWindow():
    flayout = [
        [
            gui.Titlebar(name, text_color=colour_text, background_color=colour_back)
        ]
    ]
    window = gui.Window(title=name, layout=flayout, margins=(700, 500))
    return window

def runAccount():
    log.debug(p.path_info())
    log.info("Initialising window...")
    window = runWindow(); log.info("Window succesfully initialised!")
    window.read()

def runMain(account, window):
    pass