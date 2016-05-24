from xml.dom import minidom


class DataAnalyzer:
    def __init__(self, source):
        self.doc = minidom.parse(source)

    def cost(self):
        total_cost = 0
        for data in self.doc.getElementsByTagName("data"):
            nodes = data.childNodes
            if len(nodes) > 3 and nodes[3].localName == 'cost':
                total_cost += int(nodes[3].childNodes[0].data)

        return total_cost

    def resources(self):
        """
        :return: number of resources
        """
        total_cost = 0
        data = self.doc.getElementsByTagName("data")
        data = data[0].childNodes # First data = contract + men + heading + budget
        contract = data[0]  # contract

        return len(contract)
