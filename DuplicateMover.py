#Finds and moves duplicate files in a selected folder to a "Duplicates" folder. It uses MD5 hash values for identification. The Tkinter library is used for folder selection.

from tkinter import Tk
from tkinter.filedialog import askdirectory
import os, shutil, hashlib

def DuplicateMover():
  Tk().withdraw()
  path = askdirectory(title = "Please select the folder")
  walker = os.walk(path)
  uniquefiles=dict()
  print("Don't close the program")
  for folder, sub_folder, files in walker:
    for file in files:
      filepath = os.path.join(folder, file)
      filehash = hashlib.md5(open(filepath,"rb").read()).hexdigest()

      if filehash in uniquefiles:
        shutil.move(filepath,'D:\\Duplicates\\')
        print(f"{filepath} is moved to duplicates.")
      else:
        uniquefiles[filehash]=path
      
  print("Exit code = 0\nProgram finished without errors.")

DuplicateMover()
