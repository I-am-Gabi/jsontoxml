from xml.dom import minidom
from itertools import izip  # to transform list to a dict
xml_path = 'xml/xml-output.xml'


class Resources:
    def __init__(self, source):
        self.doc = minidom.parse(source)

    def resources(self):
        """
        :return: dic of resources and amount
        """
        data = self.doc.getElementsByTagName("data")
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

    def print_resources(self):
        resources = self.resources()

        for r in resources:
            print (r + " : " + resources[r])

    def nb_resources(self):
        """
        :return: number of resources
        """
        res = self.resources()
        return len(res)


def analyzer_resource():
    a = Resources(xml_path)
    print "Number of required resources in the contract : {0}".format(a.nb_resources())
    a.print_resources()

