import os
import re


def rename_files():
    
    # 1. Get file names from random folder.
    file_list = os.listdir(r"/Users/dev/Desktop/Projects/python/secret_message/prank")
    print(file_list)
    saved_path = os.getcwd
    os.chdir(r"/Users/dev/Desktop/Projects/python/secret_message/prank")

    
    # 2. Rename file names.
    for file_name in file_list:
        os.rename(file_name,re.sub('[0-9]', '', file_name))

rename_files()
