try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Pylogenetics',
    'author': 'Dominic White',
    'url': 'https://github.com/dominicwhite/pylogenetics',
    'download_url': 'Where to download it.',
    'author_email': 'dewhite4@gmail.com',
    'version': '0.1',
    'install_requires': ['nose','networkx'],
    'packages': ['phylo'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
