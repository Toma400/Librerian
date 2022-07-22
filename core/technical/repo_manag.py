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