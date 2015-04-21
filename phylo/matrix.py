# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:16:47 2015

@author: Dominic White
"""

class CharMatrix:
    def __init__(self,name):
        self.name=name
        self.total_chars=0
        self.total_taxa=0
        self.char_names = {}
        self.taxa_names=[]
        self._taxa_indices={}
        self.chars={}
    
    def add_character(self, char_states, name=None, all_taxa=True):
        """Takes a dictionary of taxa (keys) and state (values) pairs and adds
        them to the matrix.
        If all_taxa is True (default) will raise an Exception if the taxa
        in the char_states dictionary and the CharacterMatrix do not match
        exactly."""
        if all_taxa==True:
            for taxon in self.taxa_names:
                if taxon not in char_states.keys():
                    raise Exception('The matrix contains a taxon not in the character dictionary')
            for taxon in char_states.keys():
                if taxon not in self.taxa_names:
                    raise Exception('The char dictionary contains a taxon not in the existing matrix')
        else:
            for taxon in char_states.keys():
                if taxon not in self.taxa_names:
                    self.add_taxon(taxon)
        for taxon in self.taxa_names:
            if taxon in char_states.keys():
                self.chars[taxon].append(char_states[taxon])
            else:
                self.chars[taxon].append('?')
        if name!=None:
            if type(name)!=str:
                raise Exception('Name should be a string')
            else:
                self.char_names[self.total_chars]=name
        else:
            self.char_names[self.total_chars]=self.name+'_'+str(self.total_chars)
            
        self.total_chars=self.total_chars+1
    
    def add_taxon(self, new_taxon):
        if type(new_taxon) != str:
            raise TypeError('New taxon names need to be strings')
        if new_taxon in self.taxa_names:
            raise Exception('Taxon already exists in matrix')
        self.taxa_names.append(new_taxon)
        ch = []
        for c in xrange(self.total_chars):
            ch.append('?')
        self.chars[new_taxon]=ch
        self.total_taxa=self.total_taxa+1
    
    def to_tnt(self,filename):
        f=open(filename,'w')
        f.write('xread\n')
        f.write(str(self.total_chars)+' '+str(self.total_taxa)+'\n')
        for taxon in sorted(self.chars.keys()):
            line = str(taxon).replace(' ','_') + (' '*(40-len(str(taxon))))
            for char_state in self.chars[taxon]:
                line=line + ' ' + str(char_state)
            f.write(line+'\n')
        f.write(';')
        f.close()



#m = CharMatrix('test')
#m.add_taxon('dunno')
#m.add_taxon('elephant')
#m.add_taxon('rhino')
#m.add_character({'dunno':1,'elephant':0,'rhino':4})
#m.add_character({'dunno':3,'elephant':5,'rhino':3})
#m.add_character({'dunno':0,'elephant':0,'rhino':1})
#print m.taxa_names
#print m.chars
