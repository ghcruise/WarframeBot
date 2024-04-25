import socket
import urllib
import datetime
import json
from urllib.request import urlretrieve

socket.setdefaulttimeout(10)

def recu_down(url,filename): # recurrent download with ContentTooShortError
    try:
        urlretrieve(url,filename) 
    except urllib.error.ContentTooShortError:
        print ('Network conditions is not good. Reloading...')
        recu_down(url,filename)
    except socket.timeout:
        count = 1
        while count <= 5:
            try:
                urlretrieve(url,filename)                                                
                break
            except socket.timeout:
                err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
                print(err_info)
                count += 1
        if count > 5:
            print("download job failed!")

def getWorldState():
    recu_down("http://content.warframe.com/dynamic/worldState.php", "content/worldState.json")
    with open("content/worldState.json",'r', encoding='utf-8')as f1:
        content = f1.readlines()
    #content= [line.replace('},',"},\n").replace('],','],\n').replace('Tmp\":\"','Tmp\":').replace('}"}','}}').replace('\\\"',"\"") for line in content[:]]
    #content= [line.replace('},',"},\n") for line in content[:]]
    with open("content/worldState.json",'w', encoding='utf-8')as f2:
        f2.writelines(content)
    print(f"{datetime.datetime.now()} [World] WorldState updated.")

getWorldState()