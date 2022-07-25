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