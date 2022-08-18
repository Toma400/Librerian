#-----------------|---------------------------------------------------------------------------------------------------------------------------------------
# VALUES SYSTEM   | Values are classes made to store -one mutable value- being :storage and others which are meant to remain in their initial state. The
#                 | reason for this is that other values are references to elements which should not change during program run.
#                 |
#                 | VALUE class is used as bigger dictionary, allowing for Entry arguments to not only hold a value itself, but also to contain some
#                 | elements, such as translation key for said argument or others.
#                 | SYSVALUE, in the other hand, is reserved for only few variables in Entry, and should not be changed even in terms of storage, as their
#                 | values should altogether be immutable (they are required in stable state for program to run correctly).
#-----------------|---------------------------------------------------------------------------------------------------------------------------------------
'''
    example_value = {
        val_dict:    "type_of_valdict"  # type explained below
        val_key:     ""                 # translation key
        val_storage: ---                # fixed, but usually Null by default
    }
'''

def ValueDict(vid: str, type: str, trkey: str, storage=None):
    valdict = {
        "val_id":      vid,
        "val_dict":    type,
        "val_key":     trkey,
        "val_storage": storage
    }
    return valdict

class LibrFile:

    def __init__(self, user, entry, name):
        self.user = user
        self.entry = entry
        self.name = name
        self.pav = "pathpathpath"

    def __str__(self):
        return self.name