from util import read_file_to_list

ALL_LINES = '011_all_lines.txt'
IMPORTED_LINES = '012_imported_lines.txt'
VELOCITY_TO_IMPORT = '013_vel_to_import.txt'
SEMBLANCE_TO_IMPORT = '014_semb_to_import.txt'
EG_TO_IMPORT = '015_eg_to_import.txt'

VELOCITY_TO_IMPORT2 = '013_vel_to_import2.txt'
SEMBLANCE_TO_IMPORT2 = '014_semb_to_import2.txt'
EG_TO_IMPORT2 = '015_eg_to_import2.txt'


def write_list_to_file(file_name, all_lines_list, to_import_list):
    with open(file_name, "w") as list_f:
        for line in list(set(all_lines_list) - set(to_import_list)):
            list_f.write(line + '\n')


write_list_to_file(VELOCITY_TO_IMPORT2, read_file_to_list(ALL_LINES), read_file_to_list(VELOCITY_TO_IMPORT))
write_list_to_file(SEMBLANCE_TO_IMPORT2, read_file_to_list(ALL_LINES), read_file_to_list(SEMBLANCE_TO_IMPORT))
write_list_to_file(EG_TO_IMPORT2, read_file_to_list(ALL_LINES), read_file_to_list(EG_TO_IMPORT))
