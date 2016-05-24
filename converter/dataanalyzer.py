from xml.dom import minidom

xml_path = 'xml/xml-output.xml'

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


def percentage(total, partial):
    return round((partial * 100.) / total, 2)


def analyzer():
    a = DataAnalyzer(xml_path)
    print "Total Cost : {0}".format(a.cost())
    print "Total Action : {0}".format(a.action())
    print "Percentage Action : {0}".format(a.percentage_action())