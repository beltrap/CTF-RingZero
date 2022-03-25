import urllib.request
import hashlib
from bs4 import BeautifulSoup

def getContent(url, tag, optionTag, contentPos = 0):
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), features="html.parser")

    message = soup.find(tag, optionTag).contents[contentPos]
    return message.get_text().replace('\n', '').replace(' ', '')

def getMessageHashSha512(url, tag, optionTag, contentPos = 0):
    message = getContent(url,tag,optionTag, contentPos)

    return getHashSha512(message)

def getHashSha512(content):
    return hashlib.sha512(content.encode('utf8')).hexdigest()
