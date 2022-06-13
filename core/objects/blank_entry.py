class Entry:

    # ------------------------------------------------
    # OBLIGATORY VALUES
    # ------------------------------------------------
    comment: str = ""
    tags: list = []
    #avatar: resource = None

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