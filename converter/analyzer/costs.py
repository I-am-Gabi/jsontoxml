from statistics import mean, median, mode, variance


def total_cost(data):
    total = 0
    for d in data:
        nodes = d.childNodes
        if len(nodes) > 3 and nodes[3].localName == 'cost':
            total += int(nodes[3].childNodes[0].data)
    return total


def costs(data):
    list_cost = []
    for d in data:
        nodes = d.childNodes
        if len(nodes) > 3 and nodes[3].localName == 'cost':
            list_cost.append(int(nodes[3].childNodes[0].data))
    return list_cost


def action(data):
    actions = {}
    act = ""
    take_cost = False
    for d in data:
        nodes = d.childNodes
        if len(nodes) > 1 and nodes[1].localName == 'action':
            act = nodes[1].childNodes[0].data.strip()
            take_cost = True
        if take_cost and len(nodes) > 3 and nodes[3].localName == 'cost':
            cost = int(nodes[3].childNodes[0].data)
            if act in actions:
                c = int(actions.get(act)) + cost
                item = {act: c}
                actions.update(item)
            else:
                item = {act: cost}
                actions.update(item)
    return actions


def max_action_value(cost_action):
    max_value = max(cost_action.values())
    key_max = [k for k, v in cost_action.iteritems() if v == max_value]
    return key_max, max_value


def max_action_percentage(cost_action, total):
    max_value = 0
    key_max = ""
    for k, v in cost_action.iteritems():
        p = (v * 100.) / total
        if p > max_value:
            max_value = p
            key_max = k
    return key_max, max_value


def run(data):
    c = costs(data)
    total = total_cost(data)

    print "Total Cost : {0}".format(total)

    print "Total Cost Mean: {0}".format(mean(c))

    print "Total Cost Median: {0}".format(median(c))

    print "Total Cost Mode: {0}".format(mode(c))

    print "Total Cost Variance: {0}".format(variance(c))

    cost_action = action(data)
    print "Cost by Action: "
    for k, v in cost_action.iteritems():
        print "\t{0} -> {1}".format(k, v)

    print "Percentage Cost by Action: "
    for k, v in cost_action.iteritems():
        print "\t{0} -> {1} %".format(k, round(((v * 100.) / total), 2))

    key_max, max_value = max_action_value(cost_action)
    print "More Expensive Action by value: {0} -> {1}".format(key_max[0], cost_action.get(key_max[0]))

    key_max, max_value = max_action_percentage(cost_action, total)
    print "More Expensive Action by percentage: {0} -> {1} %".format(key_max, round(max_value, 2))
