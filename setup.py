from setuptools import setup, find_packages


config = {
    'description': 'Pylogenetics',
    'author': 'Dominic White',
    'url': 'https://github.com/dominicwhite/pylogenetics',
    'download_url': 'Where to download it.',
    'author_email': 'dewhite4@gmail.com',
    'version': '0.1',
    'install_requires': ['nose','networkx','requests'],
    'packages': find_packages(),
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
