import logging
import PySimpleGUI as gui

name = "Librerian"

def run():
    gui.Window(title=name, layout=[[]], margins=(700, 500)).read()