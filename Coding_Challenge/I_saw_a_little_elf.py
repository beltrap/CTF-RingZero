#!/usr/bin/env python
from helpers import getContents, getHashMd5
from models.Tag import Tag
from base64 import b64decode


url = 'http://challenges.ringzer0team.com:10015'
content = getContents(url,[Tag("div",{"class": "message"}, 2)])

base = b64decode(content[0] + '=' * (-len(content[0]) % 4))
base = base[::-1]
md5 = getHashMd5(base)

if (md5 == content[1]):
    print('good')
else:
    print(md5 + ' ' + content[1])