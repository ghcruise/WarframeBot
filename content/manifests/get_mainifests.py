import urllib
from urllib.request import urlretrieve
import json
import os
import sys
sys.path.append(os.path.join(os.getcwd()))
from function.translate_uni2zh import uni2zh

def recu_down(url,filename): # recurrent download with ContentTooShortError
    try:
        urlretrieve(url,filename)
    except urllib.error.ContentTooShortError:
        print ('Network conditions is not good. Reloading...')
        recu_down(url,filename)

with open("content/ExportManifest.json",'r', encoding='utf-8') as f1:
    manifest_raw = json.load(f1)['Manifest']

print(len(manifest_raw))

for i in range(len(manifest_raw)):
    filename = str(i) + " " + uni2zh(manifest_raw[i]['uniqueName']) + ".png"
    url = f"http://content.warframe.com/PublicExport{manifest_raw[i]['textureLocation']}"
    recu_down(url,f"content/manifests/PNGs/{filename}")
    print(filename)