from core.technical.repo_manag import tomlm as t; settings = t("settings.toml"); s = settings["General"]; lang = s["language"]
from core.technical.repo_manag import tomlm as t; theme = t("themes/" + s["theme"] + ".toml")
from core.technical.repo_manag import tomlm as t; m = t("init.toml")
from core.technical.repo_manag import dir_lister as repo
from core.technical.repo_manag import lang_reader as langtxt
from core.technical.repo_manag import module_importer
from core.technical.repo_manag import file_lister
from core.elements.blank_entry import Entry
import PySimpleGUI as gui
import logging as log

#--------------|----------------------------------
# THEME        |
#--------------|----------------------------------
tt_text = (theme["Titlebar"])["text_colour"]
tt_back = (theme["Titlebar"])["background_colour"]
mn_text = (theme["Main"])["text_colour"]
mn_back = (theme["Main"])["background_colour"]
mn_butt = (theme["Main"])["button_colour"]
ls_text = (theme["List"])["text_colour"]
ls_back = (theme["List"])["background_colour"]
ls_high = (theme["List"])["highlight_colour"]
ls_txhg = (theme["List"])["text_highlight_colour"]
ls_scrl = (theme["List"])["scroll_colour"]

#--------------|----------------------------------
# LAYOUTS      | Used by PySimpleGUI
#--------------|----------------------------------
# LOGGING SECTION
#-------------------------------------------------
def login_layout():
    accs: list = repo("accounts/")
    layout = [
            [
                gui.Titlebar(m["name"], text_color=tt_text, background_color=tt_back)
            ],
            [
                [gui.Text(langtxt("login__choose_account", lang), text_color=mn_text, background_color=mn_back)],
                [gui.Listbox(
                    values=accs, size=(40,20), key=":AccountsListed",
                    text_color=ls_text, background_color=ls_back, highlight_text_color=ls_txhg, highlight_background_color=ls_high
                )],
                [gui.Button(langtxt("login__enter", lang), key=":EnterAccount"), gui.Button(langtxt("login__add", lang), key=":AddAccount")]
            ]
    ]
    return layout

logadd_layout = [
        [
            gui.Titlebar(m["name"], text_color=tt_text, background_color=tt_back)
        ],
        [
            [gui.Text(langtxt("login__new_account", lang), text_color=mn_text, background_color=mn_back),
             gui.In(size=(25, 1), enable_events=True, key=":NewAccountName")],
            [gui.Button(langtxt("login__confirm", lang), key=":ConfirmAccountCreation")]
        ]
]
#-------------------------------------------------
# MAIN MENU SECTION
#-------------------------------------------------
def menu_layout():
    modules = file_lister("entries/", ext="py")
    for x in modules: #| imports all modules from /entries/ folder
        x1 = x.replace("\\", "."); x2 = x1.replace("\\", ".")
        __import__(x2)
    templist = []
    for i in Entry.subclasses:
        log.info(f"Recognised entry of ID: [{i}]. Loading the entry...")
        #| Creating buttons for recognised entries
        #|____________________________________________________________________________________________________________________
        if "__" in i.entry_langkey:                                                       #| HANDLING FOR NATIVE ENTRIES     |
            templist.append(                                                              #| --------------------------------|
                [gui.Button(langtxt(i.entry_langkey, lang), key=f":{i.entry_langkey}")]   #| Takes value from lang file      |
            ) #|_____________________________________________________________________________________________________________|
        else:                                                                             #| HANDLING FOR PLUGIN ENTRIES     |
            templist.append(                                                              #| --------------------------------|
                [gui.Button(i.interior_langkey(self=i, key=i.entry_langkey, lang=lang),   #| Takes value from custom langkey |
                 key=f":{i.interior_langkey(self=i, key=i.entry_langkey, lang=lang)}")]   #| dictionaries                    |
            ) #|_____________________________________________________________________________________________________________|
    layout = [
        [
            gui.Titlebar(m["name"], text_color=tt_text, background_color=tt_back)
        ],
        [
            templist,
            [gui.Button(langtxt("menu__settings", lang), key=f":EnterSettings")],
            [gui.Button(langtxt("menu__donate", lang), key=f":Donate")],
            [gui.Button(langtxt("menu__exit", lang), key=f":Exit")]
        ]
    ]
    return layout