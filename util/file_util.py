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

def get_new_by_compare_lists(a_list, b_list):
    new_list = []
    for i in b_list:
        if i not in a_list:
            new_list.append(i)
    return new_list
