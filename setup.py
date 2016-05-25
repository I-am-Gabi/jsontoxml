try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'XmlAnalyzer',
    'author': 'CAVALCANTE and OLIVEIRA',
    'url': 'https://github.com/I-am-Gabi/jsontoxml',
    'download_url': 'https://github.com/I-am-Gabi/jsontoxml',
    'author_email': '',
    'version': '0.1',
    'requires': ['nose', 'matplotlib', 'lxml'],
    'packages': find_packages(),
    'scripts': [],
    'name': 'xmlanalyzer'
}

setup(**config)
