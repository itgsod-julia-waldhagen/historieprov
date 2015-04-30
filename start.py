 # -*- coding: utf-8 -*-
from pprint import pprint
import yaml




with open("bernadotte.yaml") as f:
    family = yaml.load(f)



#UPPGIFT 1

def name(f):
    names = []
    for k, v in f.iteritems():
        if k == 'name':
            names.append(v)
        elif k == 'consort':
            for k,v in f[k].iteritems():
                if k == 'name':
                    names.append(v)
        elif k == 'barn':
            for i in f[k]:
                names.append(name(i))
    return names

f = family['bernadotte']
print name(f)






