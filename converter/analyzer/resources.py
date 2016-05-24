from xml.dom import minidom
from itertools import izip  # to transform list to a dict
xml_path = 'xml/xml-output.xml'


def resources(data_xml):
    """
    :return: dic of resources and amount
    """
    data = minidom.parse(data_xml).getElementsByTagName("data")
    data = data[0].childNodes  # First data = contract + men + heading + budget
    contract = data[1]  # contract
    res_list = contract.childNodes  # List of amount+ resources
    count = 0
    # delete items related to tabulation
    for res in res_list:
        try:
            if res.data == "\n\t\t\t":
                del res_list[count]
        except AttributeError:
            pass
        count += 1
    # transform in dict
    # i = iter(resources)
    # r = dict(izip(i, i))
    r = {res_list[i].firstChild.data.strip(): res_list[i - 1].firstChild.data.strip() for i in
         range(1, len(res_list), 2)}
    return r


def print_resources(data_xml):
    res = resources(data_xml)

    for r in res:
        print (r + " : " + res[r])


def nb_resources(data_xml):
    """
    :return: number of resources
    """
    res = resources(data_xml)
    return len(res)


def analyzer_resource(data_xml):
    print "Number of required resources in the contract : {0}".format(nb_resources(data_xml))
    print_resources(data_xml)

