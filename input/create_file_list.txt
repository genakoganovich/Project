from os import listdir
from os.path import isfile, join

lines_file = 'full_list_of_lines.txt'
lines_file_plus_column = 'full_list_of_lines_plus_column.txt'
sgy_path = 'd:/data/sgy/'


def create_file_list(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def read_lines_to_list(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


def add_column(path, file_name, file_name_column):
    file_list = create_file_list(path)
    line_list = read_lines_to_list(file_name)
    with open(file_name_column, 'w') as file:
        for line in line_list:
            for f in file_list:
                if f.startswith(line):
                    file.write(line + '\t' + f + '\n')


if __name__ == "__main__":
    add_column(sgy_path, lines_file, lines_file_plus_column)