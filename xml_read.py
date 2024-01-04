import math
from xml.dom import minidom
import struct
from os.path import join
from util import create_file_list

SGY_PATH = '/mnt/fastssd/BE_Perth2D/900_SENT/20240104_MF-PSDM_Q_Scaled_2D/MF-PSDM_Q_Scaled'
TEMPLATE_PATH = '/mnt/fastssd/BE_Perth2D/900_SENT/20240104_MF-PSDM_Q_Scaled_2D/xml/001_template/psdm_q_scaled_text_header_template.xml'
PROJECT_INFO_PATH = '/mnt/fastssd/BE_Perth2D/900_SENT/20240104_MF-PSDM_Q_Scaled_2D/xml/002_project_info/psdm_q_scaled_project_info.xml'


class SgyAttr:
    TEXT_HEADER_SIZE = 3200
    BIN_HEADER_SIZE = 400
    S_I = 17
    S_N = 21
    DATUM = 52

    def __init__(self, path, file_name):
        self.path = path
        self.file_name = file_name
        self.full_name = join(SGY_PATH, file_name)
        self.attributes = dict()
        self.attributes['line'] = file_name[0:str(file_name).find('_')]
        self.attributes['sample_interval_depth'] = str(SgyAttr.get_s_interval_depth(self.full_name))
        self.attributes['trace_length_depth'] = str(SgyAttr.get_s_len_depth(self.full_name))
        self.attributes['sample_interval_time'] = str(SgyAttr.get_s_interval_time(self.full_name))
        self.attributes['trace_length_time'] = str(SgyAttr.get_s_len_time(self.full_name))
        self.attributes['datum'] = str(SgyAttr.get_datum(self.full_name))

    def __repr__(self):
        rep = 'Sgy(' + self.path + ', ' \
              + self.file_name + ', ' \
              + str(self.get_attribute('line')) + ', ' \
              + str(self.get_attribute('sample_interval')) + ', ' \
              + str(self.get_attribute('trace_length')) + ', ' \
              + str(self.get_attribute('datum')) + ')'
        return rep

    def get_attribute(self, key):
        return self.attributes[key]

    @staticmethod
    def get_value(file_name, position, format_character, size):
        with open(file_name, 'rb') as f:
            f.seek(position)
            return int(struct.unpack(format_character, f.read(size))[0])

    @staticmethod
    def get_s_interval_depth(file_name):
        return math.ceil(SgyAttr.get_value(file_name, SgyAttr.TEXT_HEADER_SIZE + SgyAttr.S_I,
                                           'h', 2))

    @staticmethod
    def get_s_interval_time(file_name):
        return math.ceil(SgyAttr.get_value(file_name, SgyAttr.TEXT_HEADER_SIZE + SgyAttr.S_I,
                                           'h', 2) / 1000)

    @staticmethod
    def get_s_number(file_name):
        return SgyAttr.get_value(file_name, SgyAttr.TEXT_HEADER_SIZE + SgyAttr.S_N, 'h', 2)

    @staticmethod
    def get_s_len_depth(file_name):
        return SgyAttr.get_s_interval_depth(file_name) * (SgyAttr.get_s_number(file_name))

    @staticmethod
    def get_s_len_time(file_name):
        return SgyAttr.get_s_interval_depth(file_name) * (SgyAttr.get_s_number(file_name) - 1)

    @staticmethod
    def get_datum(file_name):
        return int(
            SgyAttr.get_value(file_name, SgyAttr.TEXT_HEADER_SIZE + SgyAttr.BIN_HEADER_SIZE +
                              SgyAttr.DATUM, '>I', 4) / 100)


def create_text_header(sgy_file, template_dom, project_dom):
    result = []
    line_to_add = []
    total_width = int(template_dom.getElementsByTagName('total_width')[0].childNodes[0].data)
    left_width = int(template_dom.getElementsByTagName('left_width')[0].childNodes[0].data)

    count = 1

    for line in template_dom.getElementsByTagName('line'):
        line_to_add.append('C{0:2d}  '.format(count))

        for part in line.getElementsByTagName('part'):
            line_to_add.append(get_data_to_append(line_to_add, part, left_width, sgy_file, project_dom))

        result.append("".join(line_to_add).ljust(total_width))
        count += 1
        line_to_add.clear()

    return result


def get_data_to_append(line_parts, part, left_width, sgy_file, project_dom):
    if part.getAttribute("info").startswith('xml'):
        info_value = project_dom.getElementsByTagName(part.getAttribute("info").split()[1])[0].childNodes[0].data
        return info_value

    elif part.getAttribute("info").startswith('sgy'):
        return sgy_file.get_attribute(part.getAttribute("info").split()[1])

    elif part.getAttribute("column") == "left":
        return ' ' * (left_width - sum(map(len, line_parts)))

    else:
        return part.childNodes[0].data


def save_text_header(text_header, sgy):
    with open(sgy.full_name, 'r+b') as f:
        for line in text_header:
            f.write(line.strip().ljust(80).encode('cp500'))


def run(temp_path, info_path):
    with minidom.parse(temp_path) as template_dom, minidom.parse(info_path) as project_dom:
        for name in create_file_list(SGY_PATH):
            sgy_attr = SgyAttr(SGY_PATH, name)
            save_text_header(create_text_header(sgy_attr, template_dom, project_dom), sgy_attr)


if __name__ == '__main__':
    run(TEMPLATE_PATH, PROJECT_INFO_PATH)