from core.technical.repo_manag import tomlm as t; settings = t("settings.toml"); s = settings["General"]; lang = s["language"]
from core.technical.repo_manag import dir_lister as repo; accs: list = repo("accounts/")
from core.technical.repo_manag import lang_reader as langtxt
import logging as log
import PySimpleGUI as gui
import core.gui.menu as m

def runWindow():
    log.info("Initialising window...")
    flayout = [
        [
            gui.Titlebar(m.name, text_color=m.colour_text, background_color=m.colour_back)
        ],
        [
            [gui.Text(langtxt("login__choose_account", lang), text_color=m.colour_text)],
            [gui.Listbox(
                values=accs, size=(40,20), key=":Accounts"
            )],
            [gui.Button(langtxt("login__enter", lang))]
        ]
    ]
    window = gui.Window(title=m.name, layout=flayout, margins=(700, 500))
    return window

def closeWindow(window):
    window.close()