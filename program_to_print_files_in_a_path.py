#to print list of files in a file path
import os
directory="/"
content=os.listdir(directory)
for item in content:
    print(item)