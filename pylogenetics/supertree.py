# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:10:10 2015

@author: Dominic White
"""

import tree
import matrix


def get_desc(t,internal):
    desc=[internal]
    for d in t.successors(internal):
        desc=desc+get_desc(t,d)
    return desc

def mrp_matrix(source_trees):
    """Takes a list of nx objects.
    Turns these into a character matrix using representation with parsimony.
    Returns a Matrix object."""
    mrp=matrix.CharMatrix('MRP matrix')
    for t in source_trees:
        taxa_present = []
        for tip in t.nodes(): #Add any new taxa to the matrix
            if t.degree(tip)==1:
                taxa_present.append(tip)
                if t.node[tip]['name'] not in mrp.taxa_names:
                    mrp.add_taxon(t.node[tip]['name'])
        print taxa_present
        clusters=[]
        for node in t.nodes():
            if t.degree(node)>2:
                print node, "getting clusters"
                print get_desc(t,node)
                clusters.append(get_desc(t,node))
        print clusters
        for c in clusters:
            c_states={}
            for node in t.nodes():
                if t.degree(node)==1:
                    if node in taxa_present:
                        if node in c:
                            c_states[t.node[node]['name']]=1
                        else:
                            c_states[t.node[node]['name']]=0
                    else:
                        c_states[t.node[node]['name']]='?'
            print "Character:",c_states
            mrp.add_character(c_states, all_taxa=False)
    return mrp


