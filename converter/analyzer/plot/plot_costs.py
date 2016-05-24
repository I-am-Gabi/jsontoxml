import matplotlib.pyplot as plt


def plot_cost_action(cost_action):
    actions = []
    costs = []
    for k, v in cost_action.iteritems():
        actions.append(k)
        costs.append(v)
    x = range(0, len(actions))
    plt.xticks(x, actions)
    plt.bar(x, costs)
    plt.title("action x cost", fontsize=15)
    plt.xlabel("success")
    plt.ylabel("probability")
    plt.show()
