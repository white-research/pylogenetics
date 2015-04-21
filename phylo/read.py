# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:44:32 2015

@author: Dominic White
"""

import tree

def _newick_to_tree(newick):
    lengths=False
    if ':' in newick:
        lengths=True
    t = tree.Tree()
    current_anc=0 # current ancestor node
    current_node=1
    t.add_node(current_anc)
    x=0
    while x < len(newick): #loop to go through tree string
        if newick[x]=="(":
            t.add_edge(current_anc,current_node)
            current_anc=current_node
            current_node=current_node+1
            x=x+1
        elif newick[x] == ',':
            x=x+1
        elif newick[x] == ')':
            if x+1 < len(newick) and current_anc!=1:
                next_anc=t.predecessors(current_anc)[0]
                x=x+1
                if lengths==True:
                    bl, idx_plus = _get_branch_length(newick,x)
                    t.edge[next_anc][current_anc]['length']=bl
                    x=x+idx_plus
                current_anc=next_anc
            else:
                break
        else:
            new_taxon, idx_plus = _get_taxon_name(newick, x)
            t.add_edge(current_anc,current_node)
            t.node[current_node]['name']=new_taxon
            x=x+idx_plus
            if lengths==True:
                bl, idx_plus = _get_branch_length(newick,x)
                t.edge[current_anc][current_node]['length']=bl
                x=x+idx_plus
            current_node=current_node+1
    t.remove_node(0)
    return t

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
#        print len(newick), count+y
        if newick[count+y] == ':' or newick[count+y] == ',' or newick[count+y] == ')':
            break
        else:
            y=y+1
    if y==0:
        raise ValueError('Missing a taxon name in newick tree')
    return newick[count:count+y], y



def read_trees(filename, filetype="newick"):
    """Takes a file containing phylogenetic trees (newick format) and returns 
    a tree objects for each tree in the file.
    In the future this function should also handle tnt and nexus files."""
    trees=[]
    if filetype=="newick":
        newick = open(filename)
        lines = newick.readlines()
        for t in lines:
            ntree = t.strip().replace(';','')
            if len(ntree)>0:
                trees.append( _newick_to_tree(ntree) )
        newick.close()
    elif filetype=="tnt":
        tnt=open(filename)
        lines = tnt.readlines()
        for t in lines:
            if t[0]=='(':
                t = t.replace('*','').replace(';','').replace(' )',')').replace(')(','),(').replace(' ',',')
                trees.append(_newick_to_tree(t.strip()))
        tnt.close()
    return trees

#read_trees('/home/dominic/Desktop/scaled.tre')

#_newick_to_nx('((a,b),(c,d))')
#_newick_to_nx('((a:5,b:2):4,(c:3,d:2):7)')
#_newick_to_nx('((a:5,(ef:1,b:2):3):4,(c:3,d:2):7)')
#final = _newick_to_nx('((a:5,(ef:1,b:2):3):4,(c:3,d:2):7):3')
#final = _newick_to_nx('((a:5,(ef:1.4,b:2):3):4,(c:13.6,d:2):7)')
#for edge in final.edges():
#    print edge, final.edge[edge[0]][edge[1]]['length']
#    if final.degree(edge[1])==1:
#        print '   ',final.node[edge[1]]['name']