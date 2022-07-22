from core.elements.entries.blank_entry import Entry


class BookEntry(Entry):
    # ------------------------------------------------
    # OBLIGATORY VALUES
    # ------------------------------------------------
    book_title: str = ""
    author: str = ""

    # ------------------------------------------------
    # NON-OBLIGATORY VALUES
    # ------------------------------------------------
    # User data
    rating: int = None
    date_of_reading: int = None
    dates_of_rereading: list = []
    rereading_amount = len(dates_of_rereading)
    book_tags: list = []  # tags exclusive to books
    # can be genres tag, but can be also more broadly
    # ------------------------------------------------
    # Book data
    original_title: str = ""
    year_of_publishing: int = None
    multiple_authors: list = []

    # ------------------------------------------------
    # MAIN BODY
    # ------------------------------------------------
    def __init__(self, book_title, author):
        super().__init__()
        self.book_title = book_title
        self.author = author

    # ------------------------------------------------
    # GETTERS
    # ------------------------------------------------
    # They are used, obviously, to get specific value
    # ------------------------------------------------
    def getTitle (self):
        return self.book_title
    def getAuthor (self):
        return self.author
    # ------------------------------------------------
    def getRating (self):
        return self.rating
    def getDateOfReading (self):
        return self.date_of_reading
    def getDatesOfReading (self):
        return self.dates_of_rereading
    def getRereadingAmount (self):
        return self.rereading_amount
    def getOriginalTitle (self):
        return self.original_title
    def getYearOfPublishing (self):
        return self.year_of_publishing
    def getMultipleAuthors (self):
        return self.multiple_authors