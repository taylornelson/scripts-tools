#!/usr/bin/env python
#parse security bugs from find bugs results.xml
import lxml
from lxml import etree 

f = open('results.xml')
htmltext = f.read()
f.close()

f2 = open('security_results.xml','w+')

tree = etree.fromstring(htmltext)
for element in tree.iter():
  if element.tag == 'BugInstance':
    res = element.get('category')
    if res == 'SECURITY':
    	#print str(element)
    	#print etree.tostring(element)
    	f2.write(etree.tostring(element))
    	#for subelement in element:
    	#	print str(subelement)

f2.close()