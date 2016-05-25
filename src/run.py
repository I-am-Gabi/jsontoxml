from src.converter.xmlconverter import convert, validate
from analyzer import analyzer


def run():
    open("analyzer.log", 'w').close()

    # convert the json file to xml
    convert()

    # validate the xml file
    validate()

    # analyzer the xml data
    analyzer.run()


if __name__ == "__main__":
    run()
