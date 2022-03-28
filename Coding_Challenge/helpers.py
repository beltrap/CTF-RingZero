from sqlite3 import connect
from typing import List
import urllib.request
import hashlib
from bs4 import BeautifulSoup
from models.Tag import Tag
from re import findall

def getContent(url: str, tag: str, optionTag, contentPos = 0):
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), features="html.parser")

    message = soup.find(tag, optionTag).contents[contentPos]
    return message.get_text().replace('\n', '').replace(' ', '')

def getMessageHashSha512(url: str, tag: str, optionTag, contentPos = 0):
    message = getContent(url,tag,optionTag, contentPos)

    return getHashSha512(message)

def getHashSha512(content: str):
    return hashlib.sha512(content.encode('utf8')).hexdigest()

def getHashSha1(content: str):
    return hashlib.sha1(content.encode('utf8')).hexdigest()

def getContents(url: str, tag: Tag):
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), features="html.parser")

    contents = []
    for content in soup.findAll(tag.name, tag.optionTag):
        contents.append(findall("[\d\w]{10,}", str(content))[0])
    return contents

def getHashMd5(content):
    return hashlib.md5(content).hexdigest()