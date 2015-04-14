try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Pylogenetics',
    'author': 'Dominic White',
    'url': 'http://github.com/DominicWhite/pylogenetics',
    'download_url': 'Where to download it.',
    'author_email': 'dewhite4@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['io'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
