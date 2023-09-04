import re
import os
import json

cwd = os.getcwd()
main_path = os.path.dirname(cwd)

with  open(f"{cwd}/translate/translate_dict.json",'r',encoding='utf-8') as f1:
    translatePlanet = json.load(f1)


    def translateNode(node_raw):
        node_process = re.split(r'[()]', node_raw)
        node_name = node_process[0].rstrip()
        node = translatePlanet.get(node_name,node_name)+" "+translatePlanet.get(node_process[1],node_process[1])
        return node