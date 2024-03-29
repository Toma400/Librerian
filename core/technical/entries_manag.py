from core.elements.blank_entry import Entry
#-------------|---------------------------------------------------------------------
# SETTINGS    | This class is used as element called by menu_layout() and is meant
#             | to represent its functionalities
#-------------|---------------------------------------------------------------------
# PLANNED FEATURES:
# - all settings.toml stuff
# - full screen
# - button to clear logs (or set this to do automatically after specific number of them) >> repo_manag - logs_deleting() func
# - button to export and import user data (should have also buttons for "set desktop" which would set it there + could have custom name for file ig?
# + change account (goes back to account choice) -> can be on main menu tho, especially when stuff is pushed to single [entries] menu, instead of
#   multiple entries in menu

# -------- lib:
# - within the entry           > search through tags (shows only stuff from entry containing specific tags)
#              entry selection > search through tags (shows all elements within the tags)

#----------------------------------------------------|--------------------------------------------------------------------
# Returns all custom attribute names from the class  | Set 'limit' to type if you want to specify required type of value
#----------------------------------------------------|--------------------------------------------------------------------

def return_attr(entry: Entry.subclasses):
    temp_instance = entry()
    atrlist = [attr for attr in dir(temp_instance) if not callable(getattr(temp_instance, attr)) and not attr.startswith("__")]
    #| ^ list of variables through strings, so you need to still use getattr() function
    retlist = []
    for i in atrlist:
        j = getattr(temp_instance, i)             #| takes content from each variable
        if type(j) is dict:
            if "val_dict" in j: retlist.append(i) #| checks if variable is of ValueDict type by examining if there's "val_dict" key
    return retlist