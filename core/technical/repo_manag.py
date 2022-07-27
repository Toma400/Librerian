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

@DeprecationWarning
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
  import toml
  return toml.load(pathage)

#------------|-------------------------------------------
# LANGUAGE   |
#------------|-------------------------------------------
def lang_reader (key: str, lang="english"):
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

def lang_change (choice):
  lang = choice[0] #| ISSUES: 1. langs put in file are translated (retranslate them?) 2. dump erases comments (if this matters anymore)
  import toml; log.info(f"Changing language to: [{lang}]") #| ALSO: make reloading of stuff, so lang and theme changes happen immediately
  data = tomlm("settings.toml"); data["General"]["language"] = f"{lang}"
  with open ("settings.toml", "w") as f:
    toml.dump(data, f)

def theme_change (choice):
  theme = choice[0]
  import toml; log.info(f"Changing theme to: [{theme}]")
  data = tomlm("settings.toml"); data["General"]["theme"] = f"{theme}"
  with open("settings.toml", "w") as f:
    toml.dump(data, f)