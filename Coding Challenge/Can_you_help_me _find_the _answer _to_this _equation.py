#!/usr/bin/env python
import helpers
import re

url='http://challenges.ringzer0team.com:10032/'

content = helpers.getContent(url,"div",{"class": "message"}, 2)

regex = re.findall("[0-9a-fx]+", content)

res = int(regex[0]) + int(regex[1], 16) - int(regex[2],2)

flag = helpers.getContent(url+'/?r='+str(res),"div",{"class": "alert"})
print(flag)