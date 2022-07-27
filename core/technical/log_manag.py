import logging

#--------------------------------------
# RUN
# Default config being run, with values
# set later in this module
#--------------------------------------


def run():
    logging.basicConfig(level=logging.DEBUG, filename=name_creating(), format=format_creating())

def name_creating(name=""):
    import time
    name_list = ["logs/",
                 (time.gmtime(time.time()).tm_year), "_",
                 (time.gmtime(time.time()).tm_mon), "_",
                 (time.gmtime(time.time()).tm_mday), "_",
                 (time.gmtime(time.time()).tm_hour), "_",
                 (time.gmtime(time.time()).tm_min), "_",
                 (time.gmtime(time.time()).tm_sec), "_log.log"]
    for i in name_list:
        name = name + str(i)
    return name

def format_creating(text=""):
    format_list = ["[",
                   "%(asctime)s", "] [",
                   "%(levelname)s", "] [",
                   "%(message)s", "]"]
    for i in format_list:
        text = text + str(i)
    return text

#| Custom errors
class LibrerianError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

#| Decorators
def SoftDeprecated(func):

    def wrapper_func(*args, **kwargs):
        logging.debug(f'''
        Used function marked as SoftDeprecated: {func.__name__}.
        It is recommended to not use it, if there's a way to create code in clearer way, but this function will work normally.
        SoftDeprecation is used for features that can't be put other way, but their current implementation is code-inefficient.
        ''')
        func(*args, **kwargs)
        return func(*args, **kwargs)
        # Stuff after execution

    return wrapper_func

def Deprecated(func):

    def wrapper_func(*args, **kwargs):
        logging.debug(f'''
        Used deprecated function: {func.__name__}.
        It is recommended to not use it and update your code, as Deprecated functions are not getting any support and have most
        likely their alternatives already. Code will work, but can break in future versions.
        ''')
        func(*args, **kwargs)
        return func(*args, **kwargs)
        # Stuff after execution

    return wrapper_func