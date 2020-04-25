# Python script that let you compare the file content of 2 folders and copy the deltas to a third folder. 
# In my example I had a folder with drawings issued by the client ("Civil") that contained both standard and non standard drawings
# I had another folder that contained standard drawings only
# This script runs a comparison between the two folders and copy all the drawings that is not a part of the standard drawings to a target folder.

import os
import shutil

all_files_path = 'D:\Documents\CODING\Python\LD_Match Duplicates Script\Python\Civil'
std_files_path = 'D:\Documents\CODING\\Python\LD_Match Duplicates Script\Python\Standard Drawings'
target_files_path = 'D:\Documents\CODING\Python\LD_Match Duplicates Script\Python\Target'

all_files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(all_files_path):
    for file in f:
        all_files.append(os.path.join(r, file))

# print(all_files)

std_files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(std_files_path):
    for file in f:
        std_files.append(os.path.join(r, file))

for path_civ in all_files:
    match = True
    for path_std in std_files:
        filename_civ = os.path.basename(path_civ)
        filename_std = os.path.basename(path_std)

        name_civ = filename_civ.rsplit('.', 1)[0]
        name_std = filename_std.rsplit('.', 1)[0]

        if name_std == name_civ:
            match = True
            break
        else:
            match = False
            continue
    
    
    if match == False:
        shutil.copyfile(path_civ, target_files_path + "\\" + filename_civ)

