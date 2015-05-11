from setuptools import setup, find_packages


config = {
    'name':'pylogenetics',
    'description': 'Phylogenetic analysis tools',
    'author': 'Dominic White',
    'url': 'https://github.com/dominicwhite/pylogenetics',
    'download_url': 'https://pypi.python.org/pypi/pylogenetics/',
    'author_email': 'dewhite4@gmail.com',
    'version': '0.3.3',
    'install_requires': ['nose','networkx','requests'],
    'packages': ['pylogenetics'],
    'scripts': [],
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Operating System :: OS Independent"
        ]
}

setup(**config)
