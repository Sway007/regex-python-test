import re

f = open('substitution', 'r')
txt = f.read()

nt = re.sub('\s=\w+=', ' subs!', txt)
print(nt)