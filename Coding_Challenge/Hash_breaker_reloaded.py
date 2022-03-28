#!/usr/bin/env python
from helpers import getContents,getHashSha1, getContent
from models.Tag import Tag

url = 'http://challenges.ringzer0team.com:10057'

content = getContents(url, Tag("div", {"class":"message"},2))

hash = [ str(i) for i in range(1,99999) if getHashSha1(str(i) + content[1]) == content[0] ]

flag = getContent(url+'/?r='+hash[0],"div",{"class": "alert"})
print(flag)