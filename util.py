import os
import shutil
from os import listdir
from os.path import isfile, join


def read_file_to_list(file_name):
    with open(file_name, "r") as list_f:
        result = [str(x).strip() for x in list_f.readlines()]
    return result


def create_if_not_exists(full_name_line_folder):
    if not os.path.exists(full_name_line_folder):
        os.mkdir(full_name_line_folder)


def create_file_list(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def create_file_list_contain_word(path, word):
    return [f for f in create_file_list(path) if word in f]


def copy_file_to_folder(full_name_file, target_folder, overwrite=True):
    if overwrite or (not overwrite and not os.path.exists(full_name_file)):
        shutil.copy(full_name_file, os.path.join(target_folder, os.path.basename(full_name_file)))


def move_file_to_folder(full_name_file, target_folder, overwrite=True):
    full_target_name = os.path.basename(full_name_file)
    if overwrite or (not overwrite and not os.path.exists(full_name_file)):
        shutil.move(full_name_file, os.path.join(target_folder, full_target_name))


def find_duplication(lines):
    print(set([x for x in lines if lines.count(x) > 1]))


def remove_duplicates(lines):
    return list(set(lines))
