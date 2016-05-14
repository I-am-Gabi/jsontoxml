import json


def json_to_xml(json_obj, f, line_padding=""):
    result_list = list()

    json_obj_type = type(json_obj)

    if json_obj_type is list:
        for sub_elem in json_obj:
            result_list.append(json_to_xml(sub_elem, f, "\t" + line_padding))
        return "\n".join(result_list)

    if json_obj_type is dict:
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            result_list.append("%s<%s>" % (line_padding, tag_name))
            if "contracts" in tag_name:
                result_list.append(json_to_xml(sub_obj, f, line_padding))
            else:
                result_list.append(json_to_xml(sub_obj, f, "\t" + line_padding))
            result_list.append("%s</%s>" % (line_padding, tag_name))
        return "\n".join(result_list)

    return "%s%s" % (line_padding, json_obj)


def convert():
    with open("json-input.json") as json_file:
        json_data = json.load(json_file)

    f = open('xml-output.xml', 'w')
    converted = json_to_xml(json_data, f)
    f.write("<island-data>\n %s \n </island-data>" % converted)


if __name__ == "__main__":
    convert()
