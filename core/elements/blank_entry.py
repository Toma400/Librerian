class Entry:
    subclasses = []

    # --------------|----------------------------------------------
    # SUBCLASS      | Used to derive all inheriting classes and
    # CALLER        | list them
    # --------------|----------------------------------------------
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    # -------------------------------------------------------------
    # VALUES
    # -------------------------------------------------------------
    # MAIN VALUES
    entry_langkey = ""   #| must be overriden in extended classes
    folder_key = ""      #| name of folder created in account dir
    disabled = False     #| use only if you want to overwrite vanilla entry with custom one, so you need to set off old one
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