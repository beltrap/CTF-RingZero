#!/usr/bin/env python
import urllib.request
import hashlib
from bs4 import BeautifulSoup
                                     
url = 'http://challenges.ringzer0team.com:10013'

soup = BeautifulSoup(urllib.request.urlopen(url).read(), features="html.parser")

message = soup.find("div", {"class": "message"}).contents[2]
message = message.get_text().replace('\n', '').replace(' ', '')

encode = hashlib.sha512(message.encode('utf8')).hexdigest()

soup = BeautifulSoup(urllib.request.urlopen(url+'/?r='+encode).read(), features="html.parser")
flag = soup.find("div", {"class": "alert"}).contents[0]
print(flag)