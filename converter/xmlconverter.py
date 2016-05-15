import json


def json_to_xml(json_obj, line_padding=""):
    """
    Method to convert the json object to xml using the tag xml.
    :param json_obj:
    :param line_padding:
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


def convert():
    """
    Method to open the input file and load the converter.
    """
    with open("json-input.json") as json_file:
        json_data = json.load(json_file)

    f = open('xml-output.xml', 'w')
    f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
    f.write("<?xml-stylesheet href='xml-output.css' type='text/css'?>\n")
    f.write("<!DOCTYPE island-data SYSTEM 'xml-output.dtd'>\n")
    converted = json_to_xml(json_data)
    f.write("<island-data>\n %s \n </island-data>" % converted)


if __name__ == "__main__":
    convert()
