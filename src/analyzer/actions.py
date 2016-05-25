def action(doc):
    actions = {}
    for data in doc:
        nodes = data.childNodes
        if len(nodes) > 1 and nodes[1].localName == 'action':
            act = nodes[1].childNodes[0].data.strip()
            if act in actions:
                v = int(actions.get(act)) + 1
                item = {act: v}
                actions.update(item)
            else:
                item = {act: 1}
                actions.update(item)
    return actions


def total_action(doc):
    total = 0
    for k, v in action(doc).iteritems():
        total += v
    return total


def percentage_action(doc):
    total = total_action(doc)
    data = {}
    for k, v in action(doc).iteritems():
        data.update({k: percentage(total, v)})
    return data


def percentage(total, partial):
    return round((partial * 100.) / total, 2)


def run(doc):
    f = open("analyzer.log", 'a+')
    f.write("\n############# ACTION #############\n")
    f.write("Total Action: \n")
    for k, v in action(doc).iteritems():
        f.write("\t{0} -> {1}\n".format(k, v))
    f.write("Percentage Action: \n")
    for k, v in percentage_action(doc).iteritems():
        f.write("\t{0} -> {1} %\n".format(k, v))
    f.close()