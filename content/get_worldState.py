from urllib.request import urlretrieve

urlretrieve("http://content.warframe.com/dynamic/worldState.php", "content/worldState.json")
with open("content\worldState.json",'r', encoding='utf-8')as f1:
    content = f1.readlines()
content=[line.replace('},',"},\n").replace('],','],\n') for line in content[:]]
with open("content\worldState.json",'w', encoding='utf-8')as f2:
    f2.writelines(content)
print("WorldState updated.")
# t = [obj for obj in content['ExportWeapons'] if obj['uniqueName']=="/Lotus/Weapons/Tenno/LongGuns/PrimeSybaris/PrimeSybarisRifle"]
# print(t)