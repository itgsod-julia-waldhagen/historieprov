__author__ = 'julia.waldhagen'
# -*- coding: utf-8 -*-
from pprint import pprint
import yaml




with open("bernadotte.yaml") as f:
    family = yaml.load(f)

def consorts(f):
    for k, v in f.iteritems():
        if k == 'consort':
            for k,v in f[k].iteritems():
                if k == 'name':
                     print v
        if k == 'barn':
            for i in f[k]:
                consorts(i)

f = family['bernadotte']
consorts(f)