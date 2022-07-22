import os
import sys

########################
# LIST OF FOLDERS
########################
folders = ['core',
           'gui',
           'elements',
           'technical',
           'entries']

def initialise_path():
    for i in folders:
        fpath = os.path.join(os.path.dirname(__file__), i)
    sys.path.append(fpath)

def path_info():
    info = f"""
    ---------------------------------------------------------------------------------------
    Hello in Librerian! 
    This is program initialisation message which will prompt you all important informations
    on current processes. All further info will be wrote during program running.
    
    Printing the path of the program:
    {sys.path}
    The path should include folders named as {folders[0]}, {folders[1]}, {folders[2]} and 
    others - if those are not provided, issue with the program may be related to incorrect
    path system.
    ---------------------------------------------------------------------------------------
    """
    return info