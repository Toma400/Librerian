from core.elements.blank_entry import Entry
from core.elements.entry_values import Value
from core.technical.log_manag import Deprecated
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
@Deprecated("core.technical.entries_manag::return_attr")
def dreturn_attr(entry: Entry.subclasses, limit: type = None):
    temp_instance = entry(); atrlist = [attr for attr in dir(temp_instance) if not callable(getattr(temp_instance, attr)) and not attr.startswith("__")]
    retlist = []
    if limit is not None:
        for i in atrlist:
            print (i)
            print (type(temp_instance.return_val(i)))
            print (limit)
            if type(temp_instance.return_val(i)) == limit: retlist.append(i)
        print (retlist)
        return retlist                              #| they are returned as strings, so use return_val to use fully
    return atrlist

def return_attr(entry: Entry.subclasses):
    temp_instance = entry()
    atrlist = [attr for attr in dir(temp_instance) if not callable(getattr(temp_instance, attr)) and not attr.startswith("__")]
    retlist = []
    for i in atrlist:
        try:
            j = getattr(entry, i)
            if j.clp_id: #| checks if variable is of Value type
                retlist.append(i)
        except AttributeError:
            continue
        print (i)
        print (type(i))
    print (retlist)
    return retlist

#| they are returned as strings, so use return_val to use fully