import urllib
from urllib.request import urlretrieve
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

def recu_down(url,filename): # recurrent download with ContentTooShortError
    try:
        urlretrieve(url,filename)
    except urllib.error.ContentTooShortError:
        print ('Network conditions is not good. Reloading...')
        recu_down(url,filename)


urlretrieve("http://vmjp.voidfissure.com/index_zh.txt", "content/api_content.txt")
with open("content/api_content.txt",'r', encoding='utf-8') as f1:
    api_path = [line.rstrip() for line in f1.readlines()]

api_length = len(api_path)

api_name = [path.split('!')[0] for path in api_path]

i = 0
while i < api_length:
    PublicExport = f"http://content.warframe.com/PublicExport/Manifest/{api_path[i]}"
    recu_down(PublicExport, f"content/{api_name[i]}")
    with open(f"content\{api_name[i]}",'r', encoding='utf-8')as f2:
        content = f2.readlines()
    content=[line.replace('\\r\n',"") for line in content[:]]
    content=[line.replace('},',"},\n") for line in content[:]]
    #print(content)
    with open(f"content\{api_name[i]}",'w', encoding='utf-8')as f3:
        f3.writelines(content)
    #processing
    print(f"{str(float((i+1)/api_length)*100)} % - ({i+1}/{api_length})")
    i += 1

print("done")