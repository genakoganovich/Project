import time

from util import copy_file_to_folder

LIST_FILE = "input/022_zomf_corr_list.txt"
TARGET = "e:/data/Israel_Depth/to_import/eg/"
TARGET_FILE = "c:/output/zomf_concat.corr"
HEADER_SIZE = 1


def copy_files_from_list(list_file, target_folder):
    with open(list_file, "r") as list_f:
        for full_name_file in list_f:
            copy_file_to_folder(str(full_name_file).strip(), target_folder)
            copy_file_to_folder(str(full_name_file).strip() + ".sgy", target_folder)


def save_data(file_name, f_out, header_size):
    with open(file_name, "r") as f:
        count = 0
        for line in f:
            count += 1
            if count <= header_size:
                continue
            f_out.write(line)


def append(list_file, filename_out, header_size):
    with open(filename_out, "w") as f_out:
        with open(list_file, "r") as list_f:
            for full_name_file in list_f:
                save_data(full_name_file.strip(), f_out, header_size)


def count_lines(file_name, header_size):
    with open(file_name, "r") as f:
        count = 0
        for line in f:
            count += 1
    return count - header_size


def count_total_lines(list_file, header_size):
    count = 0
    with open(list_file, "r") as list_f:
        for full_name_file in list_f:
            count += count_lines(full_name_file.strip(), header_size)
    return count


def run():
    start_time = time.time()
    # print count_total_lines(LIST_FILE, HEADER_SIZE)
    append(LIST_FILE, TARGET_FILE, HEADER_SIZE)
    print(time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))


if __name__ == "__main__":
    run()