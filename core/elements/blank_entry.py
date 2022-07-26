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
    # PLUGIN      | If 'entry_langkey' takes value without two "__" characters, it indicates plugin entry
    # LANGKEY     | This will redirect language reading to this dict of dicts, which you should override
    #             | in similar manner, replacing keys with your custom ones, for each language supported
    #             | natively (stored in /languages/ folder).
    # -------------|---------------------------------------------------------------------------------------------
    custom_langkey = {
        "English": {
            "entry_example": "Example Translation"
        }
    }

    # -------------------------------------------------------------
    # VALUES
    # -------------------------------------------------------------
    # MAIN VALUES
    entry_langkey = ""   #| must be overridden in extended classes; plug-in users, please override it without "__" and provide translation in custom_langkey instead
    folder_key = ""      #| name of folder created in account dir; must be overridden
    disabled = False     #| use only if you want to overwrite vanilla entry with custom one, so you need to set off old one (used to edit existing entry)
    # -------------------------------------------------------------
    # NON-OBLIGATORY VALUES
    comment: str = ""    # look here ------------------------------> this can be also made in a way that instead of string, it would create new class which would
    tags: list = []      #                                           create the text file and put name referrence in .json file, so it can be read afterwards
    avatar: str = None

    # -------------------------------------------------------------
    # MAIN BODY
    # -------------------------------------------------------------
    def __init__(self):
        pass

    # -----------|-------------------------------------------------
    # GETTERS    | They are used, obviously, to get specific value
    # -----------|-------------------------------------------------
    def getComment (self):
        return self.comment
    def getTags (self):
        return self.tags
    def getAvatar (self):
        return self.avatar

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