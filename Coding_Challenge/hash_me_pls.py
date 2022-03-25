#!/usr/bin/env python
import helpers

url = 'http://challenges.ringzer0team.com:10013'
encode = helpers.getMessageHashSha512(url,"div",{"class": "message"}, 2)
flag = helpers.getContent(url+'/?r='+encode,"div",{"class": "alert"})
print(flag)