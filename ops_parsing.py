# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 23:29:33 2023

@author: Arpit Akar
"""

import xml.etree.ElementTree as ET
input= '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Arpit</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''
stuff=ET.fromstring(input)
# under users there are bunch of user find all and give it to me.
#find all gives it in list
lst=stuff.findall('users/user')
print('User count:',len(lst))
#the first user be,x=2, id,name and under id child=007 and name=arpit  
for item in lst:
    print('Name',item.find('name').text)
    print('Id',item.find('id').text)
    print('Attribiute',item.get("x"))