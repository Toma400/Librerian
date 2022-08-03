import os; gpath = os.path.dirname(os.path.abspath("main.py")); lpath = gpath + r"/languages/"
from core.technical.log_manag import SoftDeprecated, Deprecated, RequiresImprovement
import toml; import json
import logging as log

#-------------------|------------------------------------
# FILES MANAGEMENT  |
#-------------------|------------------------------------
def file_deleting (pathage):
  import os
  import shutil
  try:
    shutil.rmtree(pathage)
  except NotADirectoryError:
    os.remove(pathage)
  except PermissionError:
    que = input (f"Path {pathage} is protected. Do you want to proceed? [y?]")
    if que == "y":
      os.chmod(pathage, 0o777); os.remove(pathage)
  except FileNotFoundError:
    pass
  del shutil

def cache_deleting ():
  clist = [
    f"{gpath}/__pycache__", f"{gpath}/core/__pycache__", f"{gpath}/entries/__pycache__",
    f"{gpath}/core/__pycache__", f"{gpath}/core/elements/__pycache__", f"{gpath}/core/gui/__pycache__", f"{gpath}/core/technical/__pycache__"
  ]
  for i in clist:
    file_deleting(i)
  log.debug(f"Cache deleted successfully! Ending the program...")

@RequiresImprovement
def logs_deleting (num: int = None):
  all_logs = file_lister("logs/", "log"); all_logs.sort()
  full_num = len(all_logs); to_remove = []
  if num is not None:
    if full_num > num-1:
      delnum = full_num - (num-1); ui = 1
      for u in all_logs:
        if ui < delnum:
          to_remove.append(u); ui = ui+1
  for i in all_logs:
    try:
      if num is None: #| by default removes all logs
        file_deleting(f"{gpath}/{i}.log")
      elif full_num > num-1: #| removes only specific amount of logs
        if i in to_remove: file_deleting(f"{gpath}/{i}.log")
    except PermissionError: continue
  if num is None: log.debug("Removed all logs with request of the user.")

#-----------|--------------------------------------------
# LISTERS   | Used to list specific types of files, such
#           | as folders or entries
#-----------|--------------------------------------------
def repo_lister (path, dtype: str, ext="None"):
  if dtype == "dir": dir_lister (path)
  if dtype == "file": file_lister (path, ext)

def dir_lister (path):
  from os import listdir
  from os.path import isdir, join
  return [f for f in listdir(path) if isdir(join(path, f))]

def file_lister (path, ext="None"):
  if ext is None:
    from os import listdir
    from os.path import isfile, join
    return [f for f in listdir(path) if isfile(join(path, f))]
  else:
    import glob; listed = glob.glob(path + "*." + ext); listed2 = []
    for i in listed:
      i = i.replace(path, "")
      listed2.append(i.replace("." + ext, ""))
    return listed2

@Deprecated("__import__(module)")
#| Deprecated since this function returns objects, not
#| strings; and strings can be easily imported with
#| __import__(x) function
#|-----------------------------------------------------
def module_importer (path: str):
  #| returns list of modules, does not import
  #| use [from x import *] to make import
  import os, glob, imp; modulesdict = {}
  for path in glob.glob(f'{path}/[!_]*.py'):
    name, ext = os.path.splitext(os.path.basename(path))
    modulesdict[name] = imp.load_source(name, path)
  modules = []
  for value in modulesdict.values():
    modules.append(value)
  print(modules)
  return modules

#-------------------|------------------------------------
# TOML MANAGEMENT   |
#-------------------|------------------------------------
def tomlm (pathage: str):
  return toml.load(pathage)

#-------------------|------------------------------------
# JSON MANAGEMENT   |
#-------------------|------------------------------------
def js_read (pathage: str, key: str = None):
  try:
    with open(pathage) as jsfile: data = json.load(jsfile)
    if key is None:
      return data
    return data[key]
  except json.decoder.JSONDecodeError: log.warning(f"JSON File: {pathage} does not have any data. Skipping.")

def js_change (pathage: str, key: str, new_value):
  oldval = js_read(pathage, None)
  oldval[key] = new_value
  with open (pathage, "w") as jsfile:
    rvfile = json.dumps(oldval, indent=2)
    jsfile.write(rvfile)

def js_create (pathage: str, name: str, jsdict: dict):
  with open (f"{pathage}{name}.json", "w") as file:
    jsfile = json.dumps(jsdict, indent=2)
    file.write(jsfile)

#------------|-------------------------------------------
# LANGUAGE   |
#------------|-------------------------------------------
def lang_reader (key: str, lang="English"):
  try:
    file = tomlm(f"languages/{lang}.toml")
    return file[key]

  #| ERRORS |
  except FileNotFoundError:
    log.warning(f"Language {lang} not found, changing to default one.")
    try:
      file = tomlm("languages/English.toml")
      return file[key]
    except FileNotFoundError:
      log.critical("Default language file removed. Please redownload the software or language file.")

def lang_change (lang):
  log.info(f"Changing language to: [{lang}]")
  data = tomlm("settings.toml"); data["General"]["language"] = f"{lang}"
  with open ("settings.toml", "w") as f:
    toml.dump(data, f)

def theme_change (choice):
  theme = choice[0]
  log.info(f"Changing theme to: [{theme}]")
  data = tomlm("settings.toml"); data["General"]["theme"] = f"{theme}"
  with open("settings.toml", "w") as f:
    toml.dump(data, f)

def screen_change (choice):
  import toml; log.info(f"Changing window to: [{choice}]")
  data = tomlm("settings.toml"); data["General"]["window"] = f"{choice}"
  with open("settings.toml", "w") as f:
    toml.dump(data, f)

def log_change (choice):
  import toml; msg = ""
  try:
    ichoice = int(choice)
    if ichoice < 1: ichoice = 15; msg = " default"
  except ValueError: ichoice = 15; msg = " default"
  log.info(f"Changing log limit to{msg}: [{str(ichoice)}]")
  data = tomlm("settings.toml"); data["General"]["log_limit"] = ichoice
  with open("settings.toml", "w") as f:
    toml.dump(data, f)

#---------------------|--------------------------------------------------------------|--------------------------------------------------------------
# REVERSE ENGINEERING | Used to get language used, by searching through keys         | Lang returns language name, given value and key of toml file
# SECTION             |-----------------------------                                 |---------------------------
#                     | It is done because sometimes you can return translated word  | Warn is made to pre-check if keys repeat, so it will log
#                     | but you cannot really use it to determine the language       | that as 'warn' (as modules such as settings can work
#                     |-----------------------------                                 | incorrectly in some cases)
#                     | Created mostly to deal with PySimpleGUI/settings case        |
#---------------------|--------------------------------------------------------------|---------------------------------------------------------------
@SoftDeprecated
def reverseeng_lang (translated_value, key_assigned):
  tomllist = file_lister("languages/", "toml") #| check if this returns only names, or paths, or whatever - should only names
  for i in tomllist:
    import re; ij = re.sub(r'\\', '', i); ik = ij.replace("languages", "")
    if lang_reader(key_assigned, ik) == translated_value:
      return ik

def reverseeng_warn (key_to_check: str):
  tomllist = file_lister("languages/", "toml"); vallist = []
  for i in tomllist:
    import re; ij = re.sub(r'\\', '', i); ik = ij.replace("languages", "")
    vallist.append(lang_reader(key_to_check, ik))
  #| checking for duplicates
  j = has_duplicates(vallist)
  if j[0]:
    log.warning(f'''
    Duplicated entry found in language file for key {key_to_check}! Duplicated value takes values: {j[1]}
    Some program functions can not work correctly.
    
    Recommended solution for this is to change value of keys from printed languages (look first line of the warning) manually
    or to inform creators of those languages to change them and update the file.
    ''')

def has_duplicates (listv):
  #| code below checks for duplicated entries
  if len(listv) > len(set(listv)):
    return [True, [i for i in set(listv) if listv.count(i) > 1]]
  else:
    return [False, []]