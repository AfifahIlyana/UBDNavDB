# Runs through the 'img' folder and its subdirectories
# Writes the directory path to JSON text file
# Saves as (eg)
#   "3/img2.jpg"
#   "15/downloadw.png"

import os

# Retrieve the full path of the img directory
# The img directory should be in the same folder as this python script
pyPath = os.path.dirname(os.path.realpath(__file__)) + "\\img"
# Get and store all of the img index folders in a list
imgFolders = [f.name for f in os.scandir(pyPath) if f.is_dir()]

img_path_list = []
json = "{\"imgPath\":["

for i in imgFolders:
    path = pyPath + "\\" + i
    img_names = [f.name for f in os.scandir(path)]

    for img in img_names:
        img_path = "/" + i + "/" + img
        json = json + " \"" + img_path + "\","
        #img_path_list.append(img_path)

json = json[:-1]
json = json + "]}"
#print(json)

# Create and Write JSON File
f = open("ImagePath.json","w+")
f.write(json)
f.close()












