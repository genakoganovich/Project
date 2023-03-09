from os import listdir
from os.path import isfile, join

from util import find_duplication

DIR_PATH = '//192.168.20.233/s$/Data/IsraelProject/999_to_ftp/01 SEISMIC PROCESSING/Results_proc_2/005_MF_Map_migration/003_zomf_new_map_migration_ap3000_dec/'


def create_line_list(path):
    return [f.split('__')[0] for f in listdir(path) if isfile(join(path, f))]


if __name__ == "__main__":
    find_duplication(create_line_list(DIR_PATH))
