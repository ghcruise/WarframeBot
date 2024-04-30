import os
import sys
import json
import datetime

def getArchimedea():
    with open("content/worldState.json",'r',encoding='utf-8') as f:
        worldState_dict=json.load(f)
        archimedea_string=worldState_dict["Tmp"]
        archimedea_dict=json.loads(archimedea_string)
        print(archimedea_dict["lqo5"])
        

getArchimedea()