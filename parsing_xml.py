# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 23:13:46 2023

@author: Arpit Akar
"""

import xml.etree.ElementTree as ET
#''' is multiline writings
data='''<person>
<name>ARPIT</name>
<phone type="intl">
+917742471715
</phone>
<email hide="yes"/>
</person>'''
# fromstring convert it into readable tree
tree=ET.fromstring(data)
#get me the child of name that is arpit
print('Name:',tree.find('name').text)
element = tree.find('email')
#element has attribiutw yes with nothing inside self closing tag 
if element is not None:
    print('Attr:', element.get('hide'))
else:
    print('Email element not found.')
    #how to extract data from xml watch online