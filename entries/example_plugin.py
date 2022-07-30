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
            "entry_museums": "Museums Attended"
        },
        "Polish": {
            "entry_museums": "Museums Attended in PL!"
        },
        "Hungarian": {
            "entry_museums": "Museums Attended in HU!"
        },
        "Arabic": {
            "entry_museums": "Museums Attended in AR!"
        },
        "Spanish": {
            "entry_museums": "Museums Attended in ES!"
        }
    }
    # ------------------------------------------------
    # MAIN BODY
    # ------------------------------------------------
    def __init__(self, **kwargs):                   #| **kwargs let you pass all superclass (Entry) arguments to its constructor, therefore you don't
        super().__init__(**kwargs)                  #| need to rewrite them manually - the only variables you will need