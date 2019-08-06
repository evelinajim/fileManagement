# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 12:14:34 2019

@author: New User
"""

import os , sys
import argparse
ap = argparse.ArgumentParser(description='Check files we want to exist in the directory and that do not exist in the directory')
ap.add_argument("inputPath", help = "Path directory where the files will be checked")
ap.add_argument("--files", action='append', default=[], dest='files', help = "check files")
#convert files to list

# prints help if no arguments are provided
if len(sys.argv)==1:
    ap.print_help(sys.stderr)
    sys.exit(1)

args = vars(ap.parse_args())

###Intializers###
files = args['files'] #file user wishes to find
BaseDirectory = args['inputPath'] #directory


os.chdir(BaseDirectory)
print(os.listdir())

allFiles =[]
allFiles = os.listdir()

#os.path.exists(BaseDirectory+'/results')

fileExistsList=[]
missingFiles=[]
extraFiles=[]

for i in files:
    if os.path.exists(BaseDirectory+i)==True:
        fileExistsList.append(i)
    else:
        missingFiles.append(i)


for j in allFiles:
    if files != j:
        extraFiles.append(j)


print(extraFiles)
print(fileExistsList)
print(missingFiles)
"""
for filename in allFiles:
    
    if os.path.exists(BaseDirectory+files)==True:
       #lists = lists.append(files)
       #print(os.listdir())
       print("Files that exist: " + files)
    else:
        #lists = lists.append(filename)
        print("File does not exist" )


"""

