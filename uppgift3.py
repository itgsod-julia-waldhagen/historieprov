__author__ = 'julia.waldhagen'
from pprint import pprint
import yaml




with open("bernadotte.yaml") as f:
    family = yaml.load(f)


def name(f):
    names = []
    for k, v in f.iteritems():

            if k == 'name':
                if f['death'] is None:
                    names.append(v)
            elif k == 'consort':
                for k,v in f[k].iteritems():
                    if k == 'name':
                        if f['death'] is None:
                            names.append(v)
            elif k == 'barn':
                for i in f[k]:
                    if f['death'] is None:
                        names.append(name(i))
    return names

f = family['bernadotte']
print name(f)