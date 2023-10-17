'''
All utility methods related to file processing are defined in this file.
'''

import os


def get_dir_files_list(path="./", recursion=False):
    '''
    :param path: folder path, current file path is default
    :return: list object, listed file's path
    '''
    dir_names = os.listdir(path)
    files = []
    for dir_name in dir_names:
        absolute_path = f"{path}/{dir_name}"
        if not os.path.isdir(absolute_path):
            files.append(absolute_path)
        else:
            if recursion: # flag to control should go into a folder or not
                recursion_files_list = get_dir_files_list(absolute_path, recursion=recursion)
                files += recursion_files_list
    return files

# l = get_dir_files_list("../json", recursion=True)
# print(l)
