import operator
import requests
from bs4 import BeautifulSoup
url="http://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w"
tumkelimeler=[]
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")


def sozlukolustur(tumkelimeler):
    sozluk={}
    for kelime in tumkelimeler:
        if kelime in sozluk:
            sozluk[kelime]+=1
        else:
            sozluk[kelime]=1
    return sozluk

def kelimetemizle(tumkelimeler):
    sembolsuzkelimer=[]
    semboller="!'^#+$%&*?><|-_"+chr(775)
    for kelime in tumkelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime=kelime.replace(sembol,"")
        if (len(kelime)>0):
            sembolsuzkelimer.append(kelime)
    return sembolsuzkelimer

for kelimegrupları in soup.find_all("p"):
    icerik= kelimegrupları.text
    kelimeler=icerik.lower().split()
    for kelime in kelimeler:
        tumkelimeler.append(kelime)


tumkelimeler=kelimetemizle(tumkelimeler)
sozluk=sozlukolustur(tumkelimeler)
for anahtar,deger in sorted(sozluk.items(),key=operator.itemgetter(0)):
    print(sozluk)
