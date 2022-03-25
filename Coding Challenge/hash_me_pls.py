#!/usr/bin/env python
import urllib.request
import hashlib
from bs4 import BeautifulSoup
                                     


urlChallenge = 'http://challenges.ringzer0team.com:10013'

soup = BeautifulSoup(urllib.request.urlopen(urlChallenge).read(), features="html.parser")

message = soup.find("div", {"class": "message"}).contents[2]

encode = hashlib.sha512(message.get_text().encode('utf8')).hexdigest()

print(encode)

url = 'http://challenges.ringzer0team.com:10013='