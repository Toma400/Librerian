import logging as log
import PySimpleGUI as gui
import path_mg as p

name = "Librerian"

def runAccount():
    log.debug(p.path_info())
    log.info("Initialising window...")
    window = gui.Window(title=name, layout=[[]], margins=(700, 500)); log.info("Window succesfully initialised!")
    window.read()

def run(account):
    pass