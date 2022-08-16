from core.technical.repo_manag import tomlm as t; settings = t("settings.toml"); s = settings["General"]; lang = s["language"]; lnum = s["log_limit"]
from core.technical.repo_manag import tomlm as t; theme = t("themes/" + s["theme"] + ".toml")
from core.technical.repo_manag import tomlm as t; m = t("init.toml")
import os; spath = os.path.dirname(os.path.abspath("main.py")); fpath = spath + r"\core\icon32.png"
from core.elements.entry_values import Value
from core.technical.repo_manag import lang_reader as langtxt
from core.technical.repo_manag import dir_lister as repo
from core.technical.repo_manag import file_lister
from core.technical.entries_manag import return_attr
from core.technical.log_manag import LibrerianError
from core.elements.blank_entry import Entry
import PySimpleGUI as gui
import logging as log
import importlib

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
                gui.Titlebar(m["name"], text_color=tt_text, background_color=tt_back, icon=fpath)
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
            gui.Titlebar(m["name"], text_color=tt_text, background_color=tt_back, icon=fpath)
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
    modules = file_lister(f"entries/", ext="py")
    for x in modules: #| imports all modules from /entries/ folder
        x1 = x.replace("\\", "."); x2 = x1.replace("\\", ".")
        __import__(x2)
    templist = []
    for i in Entry.subclasses:
        log.info(f"Recognised entry of ID: [{i}]. Loading the entry...")
        #| Creating buttons for recognised entries
        #|______________________________________________________________________________________________________________________
        if "__" in i.entry_langkey:                                                             #| HANDLING FOR NATIVE ENTRIES |
            templist.append(                                                                    #| ----------------------------|
                [gui.Button(langtxt(i.entry_langkey, lang), key=f":{i.folder_key}EntryButton")] #| Takes value from lang file  |
            ) #|_______________________________________________________________________________________________________________|
        else:                                                                                   #| HANDLING FOR PLUGIN ENTRIES |
            templist.append(                                                                    #| ----------------------------|
                [gui.Button(i.interior_langkey(self=i, key=i.entry_langkey, lang=lang),         #| Takes value from            |
                 key=f":{i.folder_key}EntryButton")]   #| dictionaries                          #| custom langkey              |
            ) #|_______________________________________________________________________________________________________________|
    layout = [
        [
            gui.Titlebar(m["name"], text_color=tt_text, background_color=tt_back, icon=fpath)
        ],
        [
            templist,
            [gui.Button(langtxt("menu__settings", lang), key=f":EnterSettings")],
            [gui.Button(langtxt("menu__donate", lang), key=f":Donate")],
            [gui.Button(langtxt("menu__exit", lang), key=f":Exit")]
        ]
    ]
    return layout

def settings_layout():
    current_theme = s["theme"]
    current_winset = s["window"] #| later use to get translation + set change of window in events
    layout = [
        [
            gui.Titlebar(m["name"], text_color=tt_text, background_color=tt_back, icon=fpath)
        ],
        [
            [gui.Text(langtxt("settings__languages", lang), text_color=mn_text, background_color=mn_back),
             gui.Button(langtxt("current__language", lang), key=":ChangeLang")],
            [gui.Text(langtxt("settings__themes", lang), text_color=mn_text, background_color=mn_back),
             gui.Button(current_theme, key=":ChangeTheme")],
            [gui.Text(langtxt("settings__logs", lang), text_color=mn_text, background_color=mn_back),
             gui.Button(str(lnum), key=":LogsSet"), #| not used
             gui.Button(langtxt("settings__logs_delete", lang), key=":LogsRemove")],
            [gui.Button(langtxt("settings__confirm", lang), key=":BackToMenu")]
        ]
    ]
    return layout

def setchange_layout(el):
    #| sets layout list to languages
    if el == "lang":
        elmp = file_lister("languages/", ext="toml"); sign = "Lang"; elm = []
        for i in elmp: #| makes languages show their own names, translated
            ij = t(f"{i}.toml"); ik = ij["current__language"]
            elm.append(ik)
    #|-----------------------------
    #| sets layout list to themes
    elif el == "theme":
        import re
        elmr = file_lister("themes/", ext="toml"); sign = "Theme"; elm = []
        for i in elmr: #| makes theme show their own names without path
            ij = re.sub(r'\\', '', i); ik = ij.replace("themes", "")
            elm.append(ik)
    else: LibrerianError("Wrong parameter set on <setchange_layout> function in layouts.py file")
    #|-----------------------------
    layout = [
        [
            gui.Titlebar(m["name"], text_color=tt_text, background_color=tt_back, icon=fpath)
        ],
        [
            [gui.Text(langtxt(f"settings__{el}", lang), text_color=mn_text, background_color=mn_back)],
            [gui.Listbox(
                values=elm, size=(40, 20), key=f":{sign}Listed",
                text_color=ls_text, background_color=ls_back, highlight_text_color=ls_txhg,
                highlight_background_color=ls_high
            )],
            [gui.Button(langtxt("settings__confirm", lang), key=f":SetchangeConfirm{sign}")]
        ]
    ]
    return layout

setlog_layout = [
        [
            gui.Titlebar(m["name"], text_color=tt_text, background_color=tt_back, icon=fpath)
        ],
        [
            [gui.Text(langtxt("settings__logs_limit", lang), text_color=mn_text, background_color=mn_back),
             gui.In(size=(25, 1), enable_events=True, key=":LogsSetNumber")],
            [gui.Button(langtxt("settings__confirm", lang), key=":SetchangeConfirmLogs")]
        ]
]

#-------------------------------------------------
# ENTRY SECTION
#-------------------------------------------------
def entrylist_layout(user, entry: Entry.subclasses):
    evitems = file_lister(f"accounts/{user}/{entry.folder_key}/", "json"); eitems = []
    for i in evitems:
        i = i.replace("accounts/", ""); i = i.replace(f"{user}/", ""); i = i.replace(f"{entry.folder_key}\\", ""); i = i.replace("json", "")
        eitems.append(i)
    iditems = []
    for i in eitems:
        j = i + "ania"
        iditems.append(j)
    # this will require same treatment as previously - it will need to showcase names of the entries, but key return should be not translated nor valuated
    # because values (inside json) cannot be exclusive - imagine title being exclusive, this would be ridiculous!
    # ig there can be programs using several showcased values, check them for supportive help (like: NAME | DATE | EXTENSION, this wouldn't be possible without overriding one-keying)
    temporarily_disabled_listbox = [
            [gui.Listbox(
                values=iditems, size=(0, 20), key=f":EntryItemsId",
                text_color=ls_text, background_color=ls_back, highlight_text_color=ls_txhg,
                highlight_background_color=ls_high,
                pad=(0, 0), no_scrollbar=True
            )]
    ]
    #[gui.Column(listboxes, scrollable=True, vertical_scroll_only=True, key=f":EntryColumn")]
    listbox = [
            [gui.Listbox(
                values=eitems, size=(40, 20), key=f":EntryItemsName",
                text_color=ls_text, background_color=ls_back, highlight_text_color=ls_txhg,
                highlight_background_color=ls_high
            )]
    ]
    layout = [
        [
            gui.Titlebar(m["name"], text_color=tt_text, background_color=tt_back, icon=fpath)
        ],
        [
            listbox
        ],
        [
            [gui.Button(langtxt("entry__back_to_menu", lang), key=":BackToMenu")],
            [gui.Button(langtxt("entry__new", lang), key=":EntryNew")]
        ]
    ]
    return layout

def entryadd_layout(user, entry: Entry.subclasses):
    layvals = []; tempcl = entry()
    vallist = return_attr(entry)
    for i in vallist: #| iterates over all Value typed attrs to make their own sections on window
        valdict = getattr(tempcl, i)
        vallang = valdict["val_key"]; valid = valdict["val_id"]
        if "__" in entry.entry_langkey:                                                                                                      #------------------------
            layval = [                                                                                                                       # NATIVE ENTRIES HANDLING
                gui.Text(langtxt(vallang, lang), text_color=mn_text, background_color=mn_back),
                gui.In(size=(25, 1), enable_events=True, key=f":{valid}EntryFileCreate")
            ]
        else:                                                                                                                                #------------------------
            layval = [                                                                                                                       # PLUGIN ENTRIES HANDLING
                gui.Text(tempcl.interior_langkey(self=tempcl, key=vallang, lang=lang), text_color=mn_text, background_color=mn_back),
                gui.In(size=(25, 1), enable_events=True, key=f":{valid}EntryFileCreate")
            ]
        layvals.append(layval)
    layout = [
        [
            gui.Titlebar(m["name"], text_color=tt_text, background_color=tt_back, icon=fpath)
        ],
        [
            layvals
        ],
        [
            [gui.Button(langtxt("entry__confirm", lang), key=":EntryCreate")],
            [gui.Button(langtxt("entry__return", lang), key=f":{entry.folder_key}EntryButton")]
        ]
    ]
    return layout