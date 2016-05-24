from xml.dom import minidom
from costs import run

xml_path = 'xml/xml-output.xml'


class DataAnalyzer:
    def __init__(self, source):
        self.doc = minidom.parse(source)

    def action(self):
        actions = {}
        for data in self.doc.getElementsByTagName("data"):
            nodes = data.childNodes
            if len(nodes) > 1 and nodes[1].localName == 'action':
                act = nodes[1].childNodes[0].data.strip()
                if actions.has_key(act):
                    v = int(actions.get(act)) + 1
                    item = {act: v}
                    actions.update(item)
                else:
                    item = {act: 1}
                    actions.update(item)
        return actions

    def total_action(self):
        total_action = 0
        for k, v in self.action().iteritems():
            total_action += v
        return total_action

    def percentage_action(self):
        total = self.total_action()
        data = {}
        for k, v in self.action().iteritems():
            data.update({k: percentage(total, v)})
        return data

    def resources(self):
        """
        :return: number of resources
        """
        data = self.doc.getElementsByTagName("data")
        data = data[0].childNodes  # First data = contract + men + heading + budget
        contract = data[1]  # contract
        resources = contract.childNodes  # List of amount+ resources
        count = 0
        # delete items related to tabulation
        for res in resources:
            if res.data == "\n\t\t\t":
                del resources[count]
            count += 1
        return resources

    def nb_resources(self):
        """
        :return: number of resources
        """
        res = self.resources()
        return len(res) / 2  # 2 because its amount+resource


def percentage(total, partial):
    return round((partial * 100.) / total, 2)


def analyzer():
    a = DataAnalyzer(xml_path)
    print "Total Action : {0}".format(a.action())
    print "Percentage Action : {0}".format(a.percentage_action())
    print "Number of required resources in the contract : {0}".format(a.nb_resources())
    run(a.doc.getElementsByTagName("data"))