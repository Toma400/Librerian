from entry_values import Value, SysValue

class Entry:
    subclasses = []

    # --------------|----------------------------------------------
    # SUBCLASS      | Used to derive all inheriting classes and
    # CALLER        | list them
    # --------------|----------------------------------------------
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    # -------------|---------------------------------------------------------------------------------------------
    # PLUGIN       | If 'entry_langkey' takes value without two "__" characters, it indicates plugin entry
    # LANGKEY      | This will redirect language reading to this dict of dicts, which you should override
    #              | in similar manner, replacing keys with your custom ones, for each language supported
    #              | natively (stored in /languages/ folder).
    # -------------|-----------
    # Attention!   | If you have no translations, just copy-paste English values as a placeholder, as lack of
    #              | language key can crash the program. Look at example_plugin.py as an example.
    # -------------|---------------------------------------------------------------------------------------------
    custom_langkey = {
        "English": {
            "entry_example": "Example Translation"
        }
    }

    # ------------|----------------------------------------------------------------------------------------------
    # CONSTANT    | Those are not changeable by user and should be stated by creator of entry and stay immutable
    # VALUES      |
    # ------------|----------------------------------------------------------------------------------------------
    # Main values | Must be overridden in entries deriving
    # -----------------------------------------------------
    entry_langkey = ""   #| plug-in users, please override it without "__" and provide translation in custom_langkey instead
    folder_key    = ""   #| name of folder created in account dir, should not overlap other entries; recommended as fully lowercased
    # -----------------------------------------------------
    # Side values | Override in specific cases
    # -----------------------------------------------------
    # ? None of those yet
    # -----------------------------------------------------
    # Special     | For specific purposes, not overriding
    # -----------------------------------------------------
    disabled = False     #| change only if you want to replace vanilla entry with custom one, so you can turn off old one (should be edited in old entry)

    # ------------|----------------------------------------------------------------------------------------------
    # MAIN BODY   | While creating a plugin, you should create __init__ function using code like that:
    #             | super().__init__(*args)
    #             | Where *args should be replaced by:
    #             | - requested parameters of Entry ("user: str" is the only parameter currently requested)
    #             | - parameters requested by subclass, if you derive your plugin from other entry than default
    # ------------|----------------------------------------------------------------------------------------------
    #             | After that, you can just create bunch of self.[x] = [x] assignments and bind it to __init__
    #             | parameters. Remember that parameters without default values are obligatory for user to fill.
    #             | In general it is recommended to make default values for all parameters.
    # ------------|----------------------------------------------------------------------------------------------
    def __init__(self, comment: str = None, tags: list = None, avatar: str = None):
        #| system ones
        self.id             = "" #| there should be func taking some stuff and creating name which would be easily recognisable + exclusive no matter the data
        #| initialised during creating new item (have no default value, need to be defined)
        #| initialised optionally (have default value)
        self.comment        = Value("comment", trkey="entry__def_comment", storage=comment)
        self.tags           = Value("tags",    trkey="entry__def_tags",    storage=tags)
        self.avatar         = Value("avatar",  trkey="entry__def_avatar",  storage=avatar)       #| Name of the file, needs to be .png
        #| should have also function checking if folder within {user} exists, and if not, then create it + create the file + create
        #| images folder too +++ V look at the bottom for suggestion towards 'comment' part

    # ------------|----------------------------------------------------------------------------------------------
    # FUNCTIONS   | In most cases, plugins should leave this part of code without overriding
    # ------------|----------------------------------------------------------------------------------------------
    def write_entry(self, user: str):
        path = f"accounts/{user}/{self.folder_key}/{self.id}.json"
        pass

    def add_avatar(self, user: str):
        path = f"accounts/{user}/{self.folder_key}/images/{self.avatar}.png"
        pass

    def return_val(self, value: str): #| direct caller for value inside Value class, using strings instead of direct call
        package = getattr(self, value)
        return package

    def change_val(self, value: str, new_val, return_old=False): #| no change_sysVal as they are not meant to be changed
        #if return_old: temp = self.return_val("value") else: temp = None
        pass #| it should have .json saving here for [value.storage: new_val]
        #if return_old: return temp

    @DeprecationWarning
    def return_sysVal(self, value: str): #| direct caller for value inside SysValue class, using strings instead of direct call
        package: SysValue = getattr(self, value)
        return package

    @staticmethod
    def interior_langkey(self, key, lang="English"):
        try:
            transl_group = self.custom_langkey.get(lang)
            transl_val = transl_group.get(key)
            return transl_val
        except:
            import logging; logging.warning(f'''
            Issue with custom plugin translation has been found for entry {self}
            Entry langkey: {self.entry_langkey}
            Entry key dict: {self.custom_langkey}
            Provided key: {key}
            Provided lang: {lang}
            
            Printing the traceback:
            ''', exc_info=True)
            import traceback; traceback.print_exc()

    # -------------------------------------------------------------
    # NON-OBLIGATORY VALUES
    # comment: str = ""    # this can be also made in a way that instead of string, it would create new class which would
    # tags: list = []      # create the text file and put name referrence in .json file, so it can be read afterwards
    # avatar: str = None   #+ check if disabled constant is working