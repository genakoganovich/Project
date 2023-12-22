import xmltodict

TEMPLATE_PATH = '../input/011_template/text_header_template.xml'

with open(TEMPLATE_PATH, 'r') as file:
    xml_dict = xmltodict.parse(file.read())

print(list(xml_dict.values())[0])
