class Entry:

    entry_langkey: "" #must be overriden in extended classes
    # ------------------------------------------------
    # NON-OBLIGATORY VALUES
    # ------------------------------------------------
    comment: str = ""  # look here ----------------------------------> this can be also made in a way that instead of string, it would create new class which would
    tags: list = []  #                                                 create the text file and put name referrence in .json file, so it can be read afterwards
    avatar: str = None

    # ------------------------------------------------
    # MAIN BODY
    # ------------------------------------------------
    def __init__(self):
        pass

    #------------------------------------------------
    # GETTERS
    #------------------------------------------------
    # They are used, obviously, to get specific value
    #------------------------------------------------
    def getComment (self):
        return self.comment
    def getTags (self):
        return self.tags
    def getAvatar (self):
        return self.avatar