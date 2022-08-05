#-----------------|---------------------------------------------------------------------------------------------------------------------------------------
# VALUES SYSTEM   | Values are classes made to store -one mutable value- being :storage and others which are meant to remain in their initial state. The
#                 | reason for this is that other values are references to elements which should not change during program run.
#                 |
#                 | VALUE class is used as bigger dictionary, allowing for Entry arguments to not only hold a value itself, but also to contain some
#                 | elements, such as translation key for said argument or others.
#                 | SYSVALUE, in the other hand, is reserved for only few variables in Entry, and should not be changed even in terms of storage, as their
#                 | values should altogether be immutable (they are required in stable state for program to run correctly).
#-----------------|---------------------------------------------------------------------------------------------------------------------------------------
class RawValue:

    def __init__(self):
        pass

class Value(RawValue):

    def __init__(self, val_idf, trkey=None, storage=None, req=False):
        super().__init__()
        self.val_idf  = val_idf  #| Exclusive name for value
        self.tr_key   = trkey    #| Translation key
        self.storage  = storage  #| User input
        self.req      = req      #| Tells if it is required

class SysValue:

    def __init__(self, val_idf, storage=None, req=False):
        self.val_idf  = val_idf  # | Exclusive name for value
        self.storage  = storage  # | User input
        self.req      = req  # | Tells if it is required

class LibrFile:

    def __init__(self, user, entry, name):
        self.user = user
        self.entry = entry
        self.name = name
        self.pav = "pathpathpath"

    def __str__(self):
        return self.name