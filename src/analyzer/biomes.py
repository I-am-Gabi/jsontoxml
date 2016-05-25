def biomes(data):
    all_biomes = {}
    find = False
    total_biomes = 0
    for d in data:
        nodes = d.childNodes
        if len(nodes) > 1 and nodes[1].localName == 'action':
            act = nodes[1].childNodes[0].data.strip()
            if act == "scan":
                find = True
        if find and len(nodes) > 5 and nodes[5].localName == 'extras':
            total_biomes += 1
            find = False
            b_node = nodes[5].childNodes[1].childNodes
            list_b = b_node[0].data.split('\n\t\t\t\t')
            for b in list_b:
                biome = b.strip()
                if biome in all_biomes:
                    c = int(all_biomes.get(biome)) + 1
                    item = {biome: c}
                    all_biomes.update(item)
                elif biome != '':
                    item = {biome: 1}
                    all_biomes.update(item)
    return all_biomes, total_biomes


def percentage(b, f, total):
    f.write("\nPercentage biomes: \n")
    for k, v in b.iteritems():
        f.write("\t {0} -> {1} %\n".format(k, round((v * 100.) / total, 2)))


def run(data):
    f = open("analyzer.log", 'a+')
    f.write("\n############# BIOMES #############\n")
    b, total = biomes(data)

    f.write("Number of Scans and Biomes found: \n")
    for k, v in b.iteritems():
        f.write("\t {0} -> {1}\n".format(k, str(v)))
    percentage(b, f, total)

    f.close()
