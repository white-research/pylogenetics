from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

v='0.4.0'

config = {
    'name':'pylogenetics',
    'description': 'Phylogenetic analysis tools',
    'author': 'Dominic White',
    'url': 'https://github.com/dominicwhite/pylogenetics',
    'author_email': 'dewhite4@gmail.com',
    'version': v,
    'install_requires': ['nose','networkx','numpy','requests','pandas'],
    'long_description': long_description,
    'long_description_content_type': "text/markdown",
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
