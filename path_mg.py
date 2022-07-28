from core.technical.repo_manag import tomlm as t; m = t("init.toml")
import os; spath = os.path.dirname(os.path.abspath("main.py"))
import sys

########################
# LIST OF FOLDERS
########################
folders = [f'{spath}\\core',
           f'{spath}\\core\\gui',
           f'{spath}\\core\\elements',
           f'{spath}\\core\\technical',
           f'{spath}\\entries']

def initialise_path():
    for i in folders:
        fpath = os.path.join(i)
        sys.path.append(fpath)
    sys.path.insert(0, f'{spath}\\')

def path_info():
    info = f"""
    ---------------------------------------------------------------------------------------
    Hello in Librerian! 
    This is program initialisation message which will prompt you all important informations
    on current processes. All further info will be wrote during program running.
    
    Printing working directory of program:
    {os.getcwd()}    
    Printing the path of the program:
    {sys.path}
    The path should include folder named as {folders[0]} - if this is not provided, 
    issue with the program may be related to incorrect path system.
    
    Printing init.toml informations:
    Version:     {m["version"]} 
    Build type:  {m["status"]}
    ---------------------------------------------------------------------------------------
    """
    return info