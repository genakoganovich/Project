from util import create_file_list, read_file_to_list

lines_file = 'input/full_list_of_lines.txt'
lines_file_plus_column = 'input/full_list_of_lines_plus_column.txt'
sgy_path = 'd:/data/sgy/'


def add_column(path, file_name, file_name_column):
    file_list = create_file_list(path)
    line_list = read_file_to_list(file_name)
    with open(file_name_column, 'w') as file:
        for line in line_list:
            for f in file_list:
                if f.startswith(line):
                    file.write(line + '\t' + f + '\n')


if __name__ == "__main__":
    add_column(sgy_path, lines_file, lines_file_plus_column)