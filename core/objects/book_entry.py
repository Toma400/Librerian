from core.objects.blank_entry import Entry


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
    # ------------------------------------------------
    # Book data
    original_title: str = ""
    year_of_publishing: int = None
    multiple_authors: list = []

    # ------------------------------------------------
    # MAIN BODY
    # ------------------------------------------------
    def __init__(self):
        super().__init__()

    # ------------------------------------------------
    # GETTERS
    # ------------------------------------------------
    # They are used, obviously, to get specific value
    # ------------------------------------------------
    def getTitle(self):
        return self.book_title

    def getAuthor(self):
        return self.author