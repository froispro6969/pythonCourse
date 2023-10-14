# copyfile() = copies contents of a file
# copy()  = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata

import shutil

shutil.copyfile("text", "text2")
