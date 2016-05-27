from xml.dom import minidom

from src.analyzer import biomes, actions, costs
from src.analyzer.resources import analyzer_resource

xml_path = 'xml/xml-output.xml'

header = """
 ______     __   __     ______     __         __  __     ______     ______     ______       """ + """
/\  __ \   /\ `-.\ \   /\  __ \   /\ \       /\ \_\ \   /\___  \   /\  ___\   /\  == \      """ + """
\ \  __ \  \ \ \-.  \  \ \  __ \  \ \ \____  \ \____ \  \/_/  /__  \ \  __\   \ \  __<      """ + """
 \ \_\ \_\  \ \_\\ `\_\  \ \_\ \_\  \ \_____\  \/\_____\   /\_____\  \ \_____\  \ \_\ \_\   """ + """
  \/_/\/_/   \/_/ \/_/   \/_/\/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/ /_/    """ + """
\n\n
"""


def run():
    f = open("analyzer.log", 'a+')
    f.write(header)
    f.close()

    doc = minidom.parse(xml_path)
    actions.run(doc.getElementsByTagName("data"))
    costs.run(doc.getElementsByTagName("data"))
    biomes.run(doc.getElementsByTagName("data"))
    analyzer_resource(xml_path)
