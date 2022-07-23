import logging as log

#-------------------|----------------------
# FILES MANAGEMENT  |
#-------------------|----------------------
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

#-------------------|----------------------
# TOML MANAGEMENT   |
#-------------------|----------------------
def tomlm (pathage="theme.toml"):
  import toml
  return toml.load(pathage)

#------------|-----------------------------
# LANGUAGE   |
#------------|-----------------------------
def lang_reader (key: str, lang="english"):
  try:
    file = tomlm(f"languages/{lang}.toml")
    return file[key]

  #| ERRORS |
  except FileNotFoundError:
    log.warning(f"Language {lang} not found, changing to default one.")
    try:
      file = tomlm("languages/english.toml")
      return file[key]
    except FileNotFoundError:
      log.critical("Default language file removed. Please redownload the software or language file.")