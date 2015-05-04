# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:15:09 2015

@author: Dominic White
"""

import requests, time, random

def get_pdb_ages(taxa, time_pause=5):
    if type(taxa)!=list:
        raise Exception('The taxon names must be passed as a list')
    ages = {}
    f=open('ages'+str(604-len(taxa))+'.csv','w')
    for taxon in taxa:
        if type(taxon)!=str:
            raise Exception('Taxa must be strings')
        taxon=taxon.strip().replace('_',' ')
        age_url = 'http://paleobiodb.org/data1.1/taxa/single.json?name='+taxon+'&show=app'
        r=requests.get(age_url)
        if r.status_code != 200:
            raise Exception('Could not access paleobiodb API')
        if len(r.json()['records'])==0:
            try:
                space = taxon.index(' ')
                short_name=taxon[:space]
                print 'shortened',taxon,'to',short_name
                age_url = 'http://paleobiodb.org/data1.1/taxa/single.json?name='+short_name+'&show=app'
                r=requests.get(age_url)
                if r.status_code != 200:
                    raise Exception('Could not access paleobiodb API')
                if len(r.json()['records'])==0:
                    raise Exception('No record exist in the PaleoDB for '+str(taxon)+' or '+str(short_name))
            except:
                raise Exception('No record exist in the PaleoDB for '+str(taxon))
        
    #    print r.status_code
    #    print r.json()
        print taxon, r.json()['records'][0]['fla'], r.json()['records'][0]['lla']
        ages[taxon]=[r.json()['records'][0]['fla'],r.json()['records'][0]['lla']]
        f.write(taxon+','+str(r.json()['records'][0]['fla'])+','+str(r.json()['records'][0]['lla'])+'\n')
        wait = random.randint(0,time_pause)
        print wait
        time.sleep(wait)
    f.close()
    return ages

#taxon_list = ['Tyrannosaurus rex','Centrosaurus apertus','Stegosaurus armatus']
#print pdb_age_ranges(taxon_list)
