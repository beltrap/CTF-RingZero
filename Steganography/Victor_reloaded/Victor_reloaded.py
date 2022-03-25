from pathlib import Path
import re


p = Path(__file__).with_name('Victor_reloaded.txt')

realTxt = p.read_text('utf8')

p = Path(__file__).with_name('Victor_reloaded_fake.txt')

fakeTxt = p.read_text('utf8')

tabRealWords = re.findall('\w+',realTxt)
tabFakeWords = re.findall('\w+', fakeTxt)

listIndex = [ i for i in range(len(tabRealWords)) if tabRealWords[i] != tabFakeWords[i]]

print('<== Check diff ==>')
flag =''
for word in listIndex:
    print(tabRealWords[word] + ' : ' + tabFakeWords[word])

    if len(tabRealWords[word]) != len(tabFakeWords[word]):
        for c in tabRealWords[word]:
            i = str(tabFakeWords[word]).find(c)
            if i < 0:
                flag += c
                break
    else:
        for i in range(len(tabRealWords[word])):
            if tabRealWords[word][i] != tabFakeWords[word][i]:
                flag += tabRealWords[word][i]
                break

print('FLAG ==> '+flag)
    
