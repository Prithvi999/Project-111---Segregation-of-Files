import os
import shutil
##os.getcwd()

from_dir = "C:/Users/kalya/Downloads"
to_dir = "C:/Users/kalya/Desktop"

list_of_files = os.listdir(from_dir)
##print(list_of_files)

for files in list_of_files:
    root,ext = os.path.splitext(files)
    print("Root of the Path:", root, "Extension of the Path", ext)


