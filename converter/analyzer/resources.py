from xml.dom import minidom
from itertools import izip  # to transform list to a dict
xml_path = 'xml/xml-output.xml'


def resources(data):
    """
    :return: dic of resources and amount
    """
    data = data.doc.getElementsByTagName("data")
    data = data[0].childNodes  # First data = contract + men + heading + budget
    contract = data[1]  # contract
    resources = contract.childNodes  # List of amount+ resources
    count = 0
    # delete items related to tabulation
    for res in resources:
        try:
            if res.data == "\n\t\t\t":
                del resources[count]
        except AttributeError:
            pass
        count += 1
    # transform in dict
    # i = iter(resources)
    # r = dict(izip(i, i))
    r = {resources[i].firstChild.data.strip(): resources[i - 1].firstChild.data.strip() for i in
         range(1, len(resources), 2)}
    return r


def print_resources(data):
    res = resources(data)

    for r in res:
        print (r + " : " + res[r])


def nb_resources(data):
    """
    :return: number of resources
    """
    res = resources(data)
    return len(res)


def analyzer_resource(data):
    print "Number of required resources in the contract : {0}".format(nb_resources(data))
    print_resources(data)

