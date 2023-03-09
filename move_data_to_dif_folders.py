#   input:
#       1. txt file with file list
#       2. path to folder
#
#   for each line in txt file with file list
#       create 'line' folder
#       find all the files that contains 'line' name in file name
#       move the founded files to the created 'line' folder

from os.path import join
import util

FILES = './input/files_1.txt'
TARGET_FOLDER = 'c:/Users/gennady/PycharmProjects/output/005_folder_target/'


def run(folder, file_name):
    for line_name in util.read_file_to_list(file_name):
        util.create_if_not_exists(join(folder, line_name))

        for item in util.create_file_list_contain_word(folder, line_name):
            util.move_file_to_folder(join(folder, item), join(folder, line_name), overwrite=True)


if __name__ == "__main__":
    run(TARGET_FOLDER, FILES)
