# pylogenetics

A python package containing classes and functions for phylogenetic analyses.


Includes:
 - A tree class
 - A matrix class
 - Functions for reading tree files in newick format
 - A function for creating a MRP (supertree) matrix of a set of trees

### Installation

```
pip install pylogenetics
```

### Usage

```
import pylogenetics
```

Read tree files (in newick [default] or tnt format):

```
trees = pylogenetics.read_trees('/path/to/file.tre')
tnt_trees = pylogenetics.read_trees('/path/to/file.tnt', filetype='tnt')
```

The ```read_trees``` function returns a **list** of Tree objects (one for each tree in the input file).

The Tree class provides a wrapper around the networkx graph library, with phylogenetic helper methods:

```
tree = trees[0]
print(tree.tip_names)
tree.drop_tip(name="Tyrannosaurus rex")
tree.drop_tip(key=3)
```

Trees can be timescaled, using user defined age ranges or ages from the Paleobiology Database

```
taxon_ages = {'Tyrannosaurus': [70,65], 'Stegosaurus': [155,150], 'Saltasaurus': [70,65]}
tree.timescale(taxon_ages)
```

### License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

### Further details/citation

White, D.E. (2016) The Evolution and Phylogenetic Analysis of the Dinosaur Axial Skeleton. PhD Dissertation, George
Washington University.
