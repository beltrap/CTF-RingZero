#!/usr/bin/env python
from helpers import getContent,getHashSha1

url = 'http://challenges.ringzer0team.com:10056'

content = getContent(url, "div", {"class":"message"},2)

hash = [ str(i) for i in range(1,99999) if getHashSha1(str(i)) == content ]

flag = getContent(url+'/?r='+hash[0],"div",{"class": "alert"})
print(flag)