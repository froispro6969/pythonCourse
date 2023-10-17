import os
import shutil

path = "test.txt"

try:
    os.remove(path)
    #os.rmdir(path) # usuwa pusty folder
    #shutil.rmtree(path) # usuwa folder i wszystko co w nim jest

except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
else:
    print(path+" was deleted")