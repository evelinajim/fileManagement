# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 12:14:34 2019

@author: New User
"""

import os , sys
import argparse
ap = argparse.ArgumentParser(description='Check files we want to exist in the directory and that do not exist in the directory')
ap.add_argument("inputPath", help = "Insert directory path. What folder do you want checked")
ap.add_argument("-f","--files", action='append', default=[], dest='files', help = "Specify files to check for. Must flag -f or --files before every file specified")


# prints help if no arguments are provided
if len(sys.argv)==1:
    ap.print_help(sys.stderr)
    sys.exit(1)

args = vars(ap.parse_args())

###Intializers###
files = args['files'] #files to find
BaseDirectory = args['inputPath'] #directory


os.chdir(BaseDirectory)


allFiles =[]
allFiles = os.listdir()

print("------------------------------------------")
print("ASSIGNMENT: 7\n")
print("Files and folders within " + BaseDirectory + ":")
for i in allFiles:
    print(i)

#os.path.exists(BaseDirectory+'/results')

fileExistsList=[]
missingFiles=[]
extraFiles=[]

""" 
    * If the user input file is in the directory, append it to the fileExistsList
    * Otherwise append it to the missingFiles
"""
for i in files:
    if os.path.exists(BaseDirectory+i)==True:
        fileExistsList.append(i)
    else:
        missingFiles.append(i)


""" 
    * Checks the files indicated with the files in the directory
    * If it isn't, append it to a new list
"""
for j in allFiles:
    if j not in files:
        extraFiles.append(j)



print("------------------------------------------")
print("ASSIGNMENT: 8\n")

print("Files found: ", *fileExistsList, sep = ", ")
print("Files missing: ", *missingFiles, sep = ", ") 
print("Extra Files/Folders found: ", *extraFiles, sep = ", ")  

print("------------------------------------------")


