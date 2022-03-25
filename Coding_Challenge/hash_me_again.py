#!/usr/bin/env python
import helpers

url = 'http://challenges.ringzer0team.com:10014'
binary = helpers.getContent(url,"div",{"class": "message"}, 2)
# binary (8 bytes) to char 
message = ''.join(chr(int(binary[i:i+8],2))for i in range(0, len(binary), 8))

sha512 = helpers.getHashSha512(message)

flag = helpers.getContent(url+'/?r='+sha512,"div",{"class": "alert"})
print(flag)