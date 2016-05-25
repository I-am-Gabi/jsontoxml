import json

from lxml import etree


xml_path = 'xml/xml-output.xml'
json_path = 'json/json-raquel.json'


def json_to_xml(json_obj, line_padding=""):
    """
    Method to convert the json object to xml using the tag xml.
    :param json_obj: json object
    :param line_padding: line padding
    :return: the line_padding and the object xml
    """
    result_list = list()

    json_obj_type = type(json_obj)

    if json_obj_type is list:
        for sub_elem in json_obj:
            result_list.append(json_to_xml(sub_elem, "\t" + line_padding))
        return "\n".join(result_list)

    if json_obj_type is dict:
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            result_list.append("%s<%s>" % (line_padding, tag_name))
            if "contracts" in tag_name:
                result_list.append(json_to_xml(sub_obj, line_padding))
            else:
                result_list.append(json_to_xml(sub_obj, "\t" + line_padding))
            result_list.append("%s</%s>" % (line_padding, tag_name))
        return "\n".join(result_list)

    return "%s%s" % (line_padding, json_obj)


def header(f):
    """
    Method to set the header file.
    :param f: file object
    """
    f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
    f.write("<?xml-stylesheet href='xml-output.css' type='text/css'?>\n")
    f.write("<!DOCTYPE island-trace SYSTEM 'xml-output.dtd'>\n")


def validate():
    parser = etree.XMLParser(dtd_validation=True)
    etree.parse(xml_path, parser)


def convert():
    """
    Method to open the input file json and convert to xml.
    """

    # open the json file
    with open(json_path) as json_file:
        json_data = json.load(json_file)

    # open the xml file
    f = open(xml_path, 'w')

    # set the header file
    header(f)

    # call method to convert json file
    xml_file = json_to_xml(json_data)

    # set element root
    f.write("<island-trace>\n %s \n </island-trace>" % xml_file)

    # Close file
    f.close()

if __name__ == "__main__":
    convert()
