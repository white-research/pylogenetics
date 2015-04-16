# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 12:57:29 2014

@author: dominic
"""

import networkx as nx

debug = False

class Tree(nx.DiGraph):
    
    debug = False
    
    def __init__(self, source, debug = False):
        super(Tree,self).__init__()
        if type(source) == list:
            self.add_edges_from(source)
        if debug == True:
            self.debug = True
        
    def tips(self):
        node_list = []
        for tip in self.nodes():
            if self.degree(tip) == 1:
                node_list.append(tip)
        return node_list
    
    def root(self):
        node_list = []
        for node in self.nodes():
            if self.degree(node) == 2:
                node_list.append(node)
        if len(node_list) == 1:
            return node_list[0]
        elif len(node_list) > 1:
            print "tree has multiple roots at nodes", node_list
            return
        else:
            print "no root"
            return

    def reroot(self, outgroup):
        old_root = self.root()
    #    print 'original_root is', old_root
        outgroup_ancestor = self.predecessors(outgroup)[0]
        if old_root == outgroup_ancestor:
            return
        else:
            new_root = max(self.nodes())+1
            self.remove_edge(outgroup_ancestor, outgroup)
            self.add_edges_from([(new_root,outgroup),(new_root,outgroup_ancestor)])
            last_parent = new_root
            current_node = outgroup_ancestor
            while True:
    #            print '\ncurrent node is', current_node
    #            print 'the last_parent is', last_parent
    #            print tree.predecessors(current_node)
                parents = self.predecessors(current_node)
                for node in parents:
                    if node != last_parent:
                        parent = node
    #            print "the parent is", parent
                if parent == old_root:
    #                print 'this is the old root'
                    children = self.successors(old_root)
    #                print 'its successors are', children
    #                print 'current_node is', current_node
                    for node in children:
                        if node != current_node:
                            child = node
    #                print 'child is', child
    #                print 'the last_parent is', last_parent
                    self.remove_edges_from([(old_root,child),(old_root,current_node)])
                    self.remove_node(old_root)
                    self.add_edge(current_node,child)
    #                print 'rerooted:', tree.edges()
                    return
                else:
                    next_parent = self.predecessors(parent)[0]
                    self.remove_edge(parent,current_node)
                    self.add_edge(current_node,parent)
                    last_parent = current_node
                    current_node = parent
                    parent = next_parent

### Unit tests



if debug == True:
    testTree1 = Tree([(0,1),(0,2),(2,3),(2,4)])
    print testTree1.nodes()
    print testTree1.tips()
    print testTree1.edges()
    print type(testTree1)
    testTree2 = Tree(testTree1)
    print testTree2.nodes()

