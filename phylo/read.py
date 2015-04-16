# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:44:32 2015

@author: Dominic White
"""

import networkx as nx

def _newick_to_nx(newick):
    lengths=False
    if ':' in newick:
        lengths=True
    tree = nx.DiGraph()
    current_anc=0 # current ancestor node
    current_node=1
    tree.add_node(current_anc)
    x=0
    while x < len(newick): #loop to go through tree string
        if newick[x]=="(":
            tree.add_edge(current_anc,current_node)
            current_anc=current_node
            current_node=current_node+1
            x=x+1
        elif newick[x] == ',':
            x=x+1
        elif newick[x] == ')':
            if x+1 < len(newick) and current_anc!=1:
                next_anc=tree.predecessors(current_anc)[0]
                x=x+1
                if lengths==True:
                    bl, idx_plus = _get_branch_length(newick,x)
                    tree.edge[next_anc][current_anc]['length']=bl
                    x=x+idx_plus
                current_anc=next_anc
            else:
                break
        else:
            new_taxon, idx_plus = _get_taxon_name(newick, x)
            tree.add_edge(current_anc,current_node)
            tree.node[current_node]['name']=new_taxon
            x=x+idx_plus
            if lengths==True:
                bl, idx_plus = _get_branch_length(newick,x)
                tree.edge[current_anc][current_node]['length']=bl
                x=x+idx_plus
            current_node=current_node+1
    tree.remove_node(0)
    return tree

def _get_branch_length(newick,count): #count is the index of the colon
    if newick[count] != ':':
        raise ValueError('Expecting a colon in newick tree before branch length')
    y=0
    while True:
        if newick[count+y] == ',' or newick[count+y] == ')':
            break
        else:
            y=y+1
    if y < 2:
        raise ValueError('Missing branch length in newick tree')
    return float(newick[count+1:count+y]), y

def _get_taxon_name(newick, count):
    y=0
    while True: 
        if newick[count+y] == ':' or newick[count+y] == ',' or newick[count+y] == ')':
            break
        else:
            y=y+1
    if y==0:
        raise ValueError('Missing a taxon name in newick tree')
    return newick[count:count+y], y


def _read_newick(filename):
    newick = open(filename)
    lines = newick.readlines()
    return lines

def read_trees(filename, filetype="newick"):
    """Takes a file containing phylogenetic trees (newick format) and returns 
    a tree objects for each tree in the file.
    In the future this function should also handle tnt and nexus files."""
    lines = _read_newick(filename)
    for tree in lines:
        _newick_to_nx(tree)
    return lines

#read_trees('/home/dominic/Desktop/scaled.tre')

_newick_to_nx('((a,b),(c,d))')
_newick_to_nx('((a:5,b:2):4,(c:3,d:2):7)')
_newick_to_nx('((a:5,(ef:1,b:2):3):4,(c:3,d:2):7)')
final = _newick_to_nx('((a:5,(ef:1,b:2):3):4,(c:3,d:2):7):3')
final = _newick_to_nx('((a:5,(ef:1.4,b:2):3):4,(c:13.6,d:2):7)')
for edge in final.edges():
    print edge, final.edge[edge[0]][edge[1]]['length']
    if final.degree(edge[1])==1:
        print '   ',final.node[edge[1]]['name']