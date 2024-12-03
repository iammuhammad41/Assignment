
# Assignment 1, Ex 3.

import os
path1 = input("Enter path: ")
dirs = os.listdir(f"{path1}")
for dir in dirs:
  if(dir == "pyDir"):
    files =  os.listdir(f"{path1}/{dir}")
    for file in files:
      f = file.split("_")
      if(len(f) == 8):
        old_name = f"{path1}/{dir}/{file}"
        new_name = f[4]
        for i in range(5,8):
          new_name = new_name +"_"+f[i]
        new_name =  f"{path1}/{dir}/{new_name}"
        os.rename(old_name, new_name)