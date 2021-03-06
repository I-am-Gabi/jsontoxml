from xml.dom import minidom
from itertools import izip  # to transform list to a dict

output = "analyzer.log"


def delete_tab(list):
    count = 0
    for res in list:
        try:
            if res.data == "\n\t\t\t":
                del list[count]
        except AttributeError:
            pass
        count += 1
    return list


def resources(data_xml):
    """
    :return: dic of resources and amount
    """
    data = minidom.parse(data_xml).getElementsByTagName("data")
    data = data[0].childNodes  # First data = contract + men + heading + budget
    contract = data[1]  # contract
    res_list = contract.childNodes  # List of amount+ resources
    res_list = delete_tab(res_list) # delete items related to tabulation
    # transform into dict
    # i = iter(resources)
    # r = dict(izip(i, i))
    r = {res_list[i].firstChild.data.strip(): res_list[i - 1].firstChild.data.strip() for i in
         range(1, len(res_list), 2)}
    return r


def print_resources(data_xml):
    res = resources(data_xml)

    f = open(output, 'a+')
    for r in res:
        #  print (r + " : " + res[r])
        f.write(r + " : " + res[r] + "\n")
    f.close()


def nb_resources(data_xml):
    """
    :return: number of resources required
    """
    res = resources(data_xml)
    return len(res)


def resource_take(data_xml):
    """
    Take the resources from 'exploit' and 'transform'
    :param data_xml:
    :return:
    """
    res = {}
    # Update 'data' to 'actions
    data = minidom.parse(data_xml).getElementsByTagName("data")
    count = 0
    for d in data:
        a = delete_tab(d.childNodes)
        if d.childNodes[1].nodeName != "action" and d.childNodes[1].nodeName != "status":
            del data[count]
        count += 1

    # Take resources achieved by exploit and transform
    count = 0
    for d in data:
        if d.childNodes[1].firstChild.data.strip() == "exploit":
            resource_name = d.childNodes[3].childNodes[1].firstChild.data.strip()  # 3 to parameters; 1 to resource
            answer_exploit = data[count+1]
            if answer_exploit.childNodes[1].firstChild.data.strip() == "OK":  # 1 to status
                value = answer_exploit.childNodes[5].childNodes[1].firstChild.data.strip()  # 5 to extras; 1 to amount
                # Update res
                if resource_name in res:
                    res[resource_name] = int(res[resource_name]) + int(value)
                else:
                    res[resource_name] = int(value)

        if d.childNodes[1].firstChild.data.strip() == "transform":
            res_used = d.childNodes[3].childNodes[1]  # maybe change to list
            resource_name = res_used.localName.strip()
            value = int(res_used.childNodes[0].data.strip())
            # Update res
            try:
                if resource_name in res:
                    res[resource_name] = int(res[resource_name]) - int(value)
            except:
                print "Wrong json/xml file. Not possible transform something you don't have\n"
            # Answer of the action transform
            answer_trans = data[count+1]
            if answer_trans.childNodes[1].firstChild.data.strip() == "OK":
                extra_trans = answer_trans.childNodes[5]
                resource_name = extra_trans.childNodes[1].firstChild.data.strip()
                value = int(extra_trans.childNodes[3].firstChild.data.strip())
                # Update res
                if resource_name in res:
                    res[resource_name] = int(res[resource_name]) + int(value)
                else:
                    res[resource_name] = int(value)
        count += 1
    return res


def percentage_resouces(resources_asked, resources_caught):
    res = resources_asked
    keys = res.keys()
    for r in keys:
        if r in resources_caught:
            res[r] = int(resources_caught[r])/float(resources_asked[r])
            if res[r] >= 1:
                res[r] = 100
            else:
                res[r] = float(res[r])*100
        else :
            res[r] = 0
    return res


def analyzer_resource(data_xml):
    f = open(output, 'a+')
    f.write("\n############# RESOURCES #############\n")
    f.write("Number of required resources in the contract : {0}\n".format(nb_resources(data_xml)))
    f.write("Percentage of each resources: (caught/available) \n")
    res = percentage_resouces(resources(data_xml), resource_take(data_xml))
    rk = res.keys()
    for r in rk:
        f.write("\t" + r + "- > " + str(res[r]) + " %\n")
    f.close()
