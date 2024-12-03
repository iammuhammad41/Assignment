
# Assignment 1, Ex 2.

import os
import shutil
path1 = input("Enter path: ")
files = [ f for f in os.listdir(path1) if os.path.isfile(os.path.join(path1,f)) ]
if not os.path.isdir(f"{path1}/pyDir"):
  os.makedirs(f"{path1}/pyDir")
if not os.path.isdir(f"{path1}/txtDir"):
  os.makedirs(f"{path1}/txtDir")
if not os.path.isdir(f"{path1}/otherDir"):
  os.makedirs(f"{path1}/otherDir")

source = f"{path1}"
dest1 = f"{path1}/pyDir"
dest2 = f"{path1}/txtDir"
dest3 = f"{path1}/otherDir"
for f in files:
  if(f.endswith(".py")):
    src_path = os.path.join(source, f)
    dst_path = os.path.join(dest1, f)
    shutil.move(src_path, dst_path)
  elif(f.endswith(".txt")):
    src_path = os.path.join(source, f)
    dst_path = os.path.join(dest2, f)
    shutil.move(src_path, dst_path)
  else:
    src_path = os.path.join(source, f)
    dst_path = os.path.join(dest3, f)
    shutil.move(src_path, dst_path)
dirs = os.listdir(f"{path1}")
for d in dirs:
  files = os.listdir(f"{path1}/{d}")
  for f in files:
    print(f"{path1}/{d}/{f}")