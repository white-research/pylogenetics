# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 12:57:29 2014

@author: dominic
"""

import networkx as nx

class Tree(nx.DiGraph):
    
    def drop_tip(self, tip_name):
        in_tree=False
        for tip in self.tip_keys():
            if self.node[tip]['name']==tip_name:
                tip_num = tip
                in_tree=True
        if in_tree==False:
            raise Exception('Tip not in tree')
        anc = self.predecessors(tip_num)[0]
        anc_of_anc = self.predecessors(anc)[0]
        descs_of_anc = self.successors(anc)
        if len(descs_of_anc) >2:
            self.remove_edge(anc, tip_num)
        else:
            for d in descs_of_anc:
                if d != tip_num:
                    other_desc = d
            new_bl=None
            if self.is_timescaled():
                new_bl = self.edge[anc_of_anc][anc]['length']+self.edge[anc][other_desc]['length']
            self.remove_edge(anc,tip_num)
            self.remove_node(anc)
            self.add_edge(anc_of_anc, other_desc)
            if new_bl != None:
                self.edge[anc_of_anc][other_desc]['length']=new_bl
            
    
    def is_binary(self):
        tips=self.tip_keys()
        for n in self.nodes():
            if n not in tips:
                if len(self.successors(n)) != 2:
                    return False
        return True
    
    def is_timescaled(self):
        for b in self.edges():
            try:
                if type(self.edge[b[0]][b[1]]['length'])!=float or type(self.edge[b[0]][b[1]]['length'])!=int:
                    raise Exception('Tree has a non integer/float branch length')
            except:
                return False
        return True
    
    def reroot(self, outgroup):
        old_root = self.root()
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
                parents = self.predecessors(current_node)
                for node in parents:
                    if node != last_parent:
                        parent = node
                if parent == old_root:
                    children = self.successors(old_root)
                    for node in children:
                        if node != current_node:
                            child = node
                    self.remove_edges_from([(old_root,child),(old_root,current_node)])
                    self.remove_node(old_root)
                    self.add_edge(current_node,child)
                    return
                else:
                    next_parent = self.predecessors(parent)[0]
                    self.remove_edge(parent,current_node)
                    self.add_edge(current_node,parent)
                    last_parent = current_node
                    current_node = parent
                    parent = next_parent
    
    def root(self):
        node_list = []
        for node in self.nodes():
            if self.degree(node) == 2:
                node_list.append(node)
        if len(node_list) == 1:
            return node_list[0]
        elif len(node_list) > 1:
            raise Exception("Tree has multiple roots")
        else:
            raise Exception("Tree has no root")    
    
    def timescale(self, ages, min_l=1, r=None):
        """
        Takes a dictionary of tip ages for each tip. Keys are the tip names.
        Values for each tip are a list: [earliest appearance,last appearance].
        
        Optional arguments:
        min_l: minimum branch length. Default 1. Should be an integer or float
        greater than 0.
        """
        if r == None:
            r=self.root()
            new_ages = {}
            for t in self.tip_keys():
                try:
                    new_ages[t]=ages[self.node[t]['name']]
                except:
                    error_name='No taxon named '+str(ages[self.node[t]['name']])+' in ages dictionary'
                    raise Exception(error_name)
            ages=new_ages
        # pass 1
        descs = self.successors(r)
        if len(descs) == 0: # if the current node is a tip
            print 'at node',r,'with descendents',descs
            a = self.predecessors(r)[0]
            print '  current:',r,'ancestor:',a
            anc_age = ages[r][0]
            ages[r]=ages[r][1]
            print '  age of this node:',ages[r]
            return anc_age
        else:
            desc_ages=[]
            for d in descs:
                d_age_est = self.timescale(ages, min_l, d)
                if r not in ages.keys():
                    ages[r] = d_age_est
                else:
                    if ages[r] < d_age_est:
                        ages[r] = d_age_est    
                desc_ages.append(ages[d])
            print 'at node',r,'with descendents',descs
            print '  orig age of',r,':',ages[r]
            oldest_desc=max(desc_ages)
            print '  oldest desc age:',oldest_desc
            if ages[r] < oldest_desc+min_l:
                ages[r] = oldest_desc+min_l
            print '  new age of',r,':',ages[r]
            for idx, d in enumerate(descs):
                self.edge[r][d]['length'] = ages[r] - ages[d]
            return ages[r]
    
    def tip_keys(self):
        node_list = []
        for tip in self.nodes():
            if self.degree(tip) == 1:
                node_list.append(tip)
        return node_list
    
    def tip_names(self):
        tip_list = []
        for tip in self.nodes():
            if self.degree(tip) == 1:
                tip_list.append(self.node[tip]['name'])
        return tip_list    
    
    def __check_branching__(self):
        r = self.root()
        tips = self.tip_keys()
        for n in self.nodes():
            if n!=r:
                if len(self.predecessors(n)) == 1:
                    raise Exception("A node has more than one ancestor")
                if n not in tips:
                    if len(self.successors(n)) <2:
                        raise Exception("An interior node has too few descendents")
    
    def __repr__(self):
        return "Tree()"
    
    def __str__(self):
        return "Tree with "+str(len(self.tip_keys()))+" tips"

