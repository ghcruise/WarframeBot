import urllib
from urllib.request import urlretrieve
import json
def recu_down(url,filename): # recurrent download with ContentTooShortError
    try:
        urlretrieve(url,filename)
    except urllib.error.ContentTooShortError:
        print ('Network conditions is not good. Reloading...')
        recu_down(url,filename)

recu_down("https://warframe.huijiwiki.com/api.php?action=query&format=json&prop=revisions&titles=Data%3AUserDict.json&formatversion=2&rvprop=content&rvlimit=1","translate/wiki_translations.json")

with open("translate/wiki_translations.json",'r',encoding='utf-8')as f:
    content = json.load(f)
    content = content['query']['pages'][0]['revisions'][0]['content']
with open("translate/wiki_translations.json",'w',encoding='utf-8')as f:
    f.writelines(content)
del content

with open("translate/wiki_translations.json",'r',encoding='utf-8')as f:
    content = f.readlines()
content = [line.replace('",','",\n') for line in content[:]]
with open("translate/wiki_translations.json",'w',encoding='utf-8')as f:
    f.writelines(content)

print("done")