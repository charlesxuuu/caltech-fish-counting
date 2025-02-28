# generate txt files for folder list for preparing yolo training

import glob

folder_list = glob.glob("D:\sonar\datasets\caltech-data\kenai-train\*")
folder_prefix = "D:\sonar\datasets\caltech-data"    # len =

with open(r'D:\sonar\datasets\caltech-data\folder-in-kenai-train.txt', 'w') as fp:
    for folder in folder_list:
        # write each item on a new line
        fp.write("  - %s\n" % folder.replace("\\", "/"))
    fp.close()
    print('folder-in-kenai-train.txt output done.')


with open(r'D:\sonar\datasets\caltech-data\relative-folder-in-kenai-train.txt', 'w') as fp:
    for folder in folder_list:
        # write each item on a new line
        fp.write("  - %s\n" % folder[len(folder_prefix) + 1:].replace("\\", "/"))
    fp.close()
    print('relative-folder-in-kenai-train.txt output done.')

folder_list = glob.glob("D:\sonar\datasets\caltech-data\kenai-val\*")
folder_prefix = "D:\sonar\datasets\caltech-data"    # len =

with open(r'D:\sonar\datasets\caltech-data\folder-in-kenai-val.txt', 'w') as fp:
    for folder in folder_list:
        # write each item on a new line
        fp.write("  - %s\n" % folder.replace("\\", "/"))
    fp.close()
    print('folder-in-kenai-val.txt output done.')


with open(r'D:\sonar\datasets\caltech-data\relative-folder-in-kenai-val.txt', 'w') as fp:
    for folder in folder_list:
        # write each item on a new line
        fp.write("  - %s\n" % folder[len(folder_prefix) + 1:].replace("\\", "/"))
    fp.close()
    print('relative-folder-in-kenai-val.txt output done.')