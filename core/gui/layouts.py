from core.technical.repo_manag import tomlm as t; settings = t("settings.toml"); s = settings["General"]; lang = s["language"]
from core.technical.repo_manag import tomlm as t; theme = t("themes/" + s["theme"] + ".toml")
from core.technical.repo_manag import dir_lister as repo; accs: list = repo("accounts/")
from core.technical.repo_manag import lang_reader as langtxt
import PySimpleGUI as gui
import main as m

#--------------|----------------------------------
# THEME        |
#--------------|----------------------------------
tt_text = (theme["Titlebar"])["text_colour"]
tt_back = (theme["Titlebar"])["background_colour"]

#--------------|----------------------------------
# LAYOUTS      |
#--------------|----------------------------------
login_layout = [
        [
            gui.Titlebar(m.name, text_color=tt_text, background_color=tt_back)
        ],
        [
            [gui.Text(langtxt("login__choose_account", lang), text_color=tt_text)],
            [gui.Listbox(
                values=accs, size=(40,20), key=":Accounts"
            )],
            [gui.Button(langtxt("login__enter", lang)), gui.Button(langtxt("login__add", lang))]
        ]
]