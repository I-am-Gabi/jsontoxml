from xml.dom import minidom

from src.analyzer import biomes, actions, costs
from src.analyzer.resources import analyzer_resource

xml_path = 'xml/xml-output.xml'

header = """
 ________  ________  ________  ___           ___    ___ ________  ___  ________        """ + """
|\   __  \|\   __  \|\   __  \|\  \         |\  \  /  /|\   ____\|\  \|\   ____\       """ + """
\ \  \|\  \ \  \\ \  \ \  \|\  \ \  \        \ \  \/  / | \  \___|\ \  \ \  \___|_     """ + """
 \ \   __  \ \  \\ \  \ \   __  \ \  \        \ \    / / \ \_____  \ \  \ \_____  \    """ + """
  \ \  \ \  \ \  \\ \  \ \  \ \  \ \  \____    \/   / /   \|____|\  \ \  \|____|\  \   """ + """
   \ \__\ \__\ \__\\ \__\ \__\ \__\ \_______\__/   / /      ____\_\  \ \__\____\_\  \  """ + """
    \|__|\|__|\|__| \|__|\|__|\|__|\|_______|\___/ /       |\________\|__|\_________\ """ + """
                                            \|___|/        \|_________|   \|_________| """ + """

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
