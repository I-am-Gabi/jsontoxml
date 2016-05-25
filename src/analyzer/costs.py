from statistics import mean, median, mode, variance

from src.analyzer.plot.plot_costs import plot_cost_action


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


def costs_action(data, action):
    total = []
    take_cost = False
    for d in data:
        nodes = d.childNodes
        if len(nodes) > 1 and nodes[1].localName == 'action':
            act = nodes[1].childNodes[0].data.strip()
            if act == action:
                take_cost = True
        if take_cost and len(nodes) > 3 and nodes[3].localName == 'cost':
            take_cost = False
            cost = int(nodes[3].childNodes[0].data)
            total.append(cost)
    return total


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
            take_cost = False
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
    f = open("analyzer.log", 'a+')
    c = costs(data)
    total = total_cost(data)
    f.write("\n############# COST #############\n")
    f.write("Total Cost : {0}\n".format(total))
    f.write("Total Cost Mean: {0}\n".format(mean(c)))
    f.write("Total Cost Median: {0}\n".format(median(c)))
    f.write("Total Cost Mode: {0}\n".format(mode(c)))
    f.write("Total Cost Variance: {0}\n".format(variance(c)))

    cost_action = action(data)
    f.write("Cost by Action: \n")
    for k, v in cost_action.iteritems():
        f.write("\t{0} -> {1} units\n".format(k, v))

    f.write("Percentage Cost by Action: \n")
    for k, v in cost_action.iteritems():
        f.write("\t{0} -> {1} %\n".format(k, round(((v * 100.) / total), 2)))

    f.write("Cost Variance by Action: \n")
    for k, v in cost_action.iteritems():
        c_action = costs_action(data, k)
        if len(c_action) > 1:
            f.write("\t{0} -> {1} units\n".format(k, round(variance(c_action), 2)))
        else:
            f.write("\t{0} -> {1} units\n".format(k, round(c_action[0], 2)))

    key_max, max_value = max_action_value(cost_action)
    f.write("More Expensive Action by value: {0} -> {1}\n".format(key_max[0], cost_action.get(key_max[0])))

    key_max, max_value = max_action_percentage(cost_action, total)
    f.write("More Expensive Action by percentage: {0} -> {1} %\n".format(key_max, round(max_value, 2)))

    f.close()

    # plot_cost_action(cost_action)
