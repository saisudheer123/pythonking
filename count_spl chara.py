import re
nom=raw_input()
ne=re.sub('[\w]+','', nom)
print(len(ne))
