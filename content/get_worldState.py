import urllib
import datetime
from urllib.request import urlretrieve

def recu_down(url,filename): # recurrent download with ContentTooShortError
    try:
        urlretrieve(url,filename)
    except urllib.error.ContentTooShortError:
        print ('Network conditions is not good. Reloading...')
        recu_down(url,filename)

def getWorldState():
    recu_down("http://content.warframe.com/dynamic/worldState.php", "content/worldState.json")
    with open("content/worldState.json",'r', encoding='utf-8')as f1:
        content = f1.readlines()
    content=[line.replace('},',"},\n").replace('],','],\n') for line in content[:]]
    with open("content/worldState.json",'w', encoding='utf-8')as f2:
        f2.writelines(content)
    print(f"{datetime.datetime.now()} [World] WorldState updated.")
getWorldState()
# t = [obj for obj in content['ExportWeapons'] if obj['uniqueName']=="/Lotus/Weapons/Tenno/LongGuns/PrimeSybaris/PrimeSybarisRifle"]
# print(t)