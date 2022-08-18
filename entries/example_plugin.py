from core.elements.entry_values import ValueDict
from core.elements.blank_entry import Entry
#---------------------------------------------------------------------------------------------------------------------------
''' 
                                            EXAMPLE PLUGIN FILE
This file is made as an example on how to make plugin entries for Librerian. You will need to refer to Entry documentation
nevertheless, since all use of its elements are explained there. Vanilla entries and guide.html file can also be really
valuable sources to look into, showcasing or explaining implementation of custom entries.
'''
#---------------------------------------------------------------------------------------------------------------------------

class ExamplePlugin(Entry):
    entry_langkey = "entry_museums"
    folder_key = "museums"

    custom_langkey = {
        "English": {
            "entry_museums":     "Museums Attended",
            "entry_museums_new": "museum entry", #| used for "Creating new..." menu (has to be always entry_langkey + _new)

            "value_venue":      "Museum Venue",
            "value_exhibition": "Exhibition Name",
            "value_time":       "Visited at day"
        },
        "Polish": {
            "entry_museums":     "Museums Attended in PL!",
            "entry_museums_new": "Museum Entry", #| used for "Creating new..." menu (has to be always entry_langkey + _new)


            "value_venue":       "Museum Venue",
            "value_exhibition":  "Exhibition Name",
            "value_time":        "Visited at day"
        },
        "Hungarian": {
            "entry_museums":     "Museums Attended in HU!",
            "entry_museums_new": "Museum Entry", #| used for "Creating new..." menu (has to be always entry_langkey + _new)

            "value_venue":       "Museum Venue",
            "value_exhibition":  "Exhibition Name",
            "value_time":        "Visited at day"
        },
        "Arabic": {
            "entry_museums":     "Museums Attended in AR!",
            "entry_museums_new": "Museum Entry", #| used for "Creating new..." menu (has to be always entry_langkey + _new)

            "value_venue":       "Museum Venue",
            "value_exhibition":  "Exhibition Name",
            "value_time":        "Visited at day"
        },
        "Spanish": {
            "entry_museums":     "Museums Attended in ES!",
            "entry_museums_new": "Museum Entry", #| used for "Creating new..." menu (has to be always entry_langkey + _new)

            "value_venue":       "Museum Venue",
            "value_exhibition":  "Exhibition Name",
            "value_time":        "Visited at day"
        }
    }
    # ------------------------------------------------
    # MAIN BODY
    # ------------------------------------------------
    def __init__(self, venue: str = None, exhibition: str = None, vtime=None, **kwargs):
        super().__init__(**kwargs)
        self.venue      = ValueDict(vid="venue", type="text", trkey="value_venue", storage=venue)
        self.exhibition = ValueDict(vid="exhibition", type="text", trkey="value_exhibition", storage=exhibition)
        self.time       = ValueDict(vid="vtime", type="text", trkey="value_time", storage=vtime) #| time should have different type?