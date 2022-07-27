from core.elements.blank_entry import Entry


class BookEntry(Entry):
    entry_langkey = "entry__book"
    folder_key = "books"
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
    series: dict = {} # key = name of series, value = number

    # ------------------------------------------------
    # MAIN BODY
    # ------------------------------------------------
    def __init__(self, user: str):
        super().__init__(user=user)
        #self.book_title = book_title
        #self.author = author