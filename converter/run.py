from converter.dataanalyzer import analyzer
from converter.xmlconverter import convert, validate


def run():
    # convert
    convert()

    # validation
    validate()

    # analyzer
    analyzer()

if __name__ == "__main__":
    run()