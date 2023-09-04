#该算法导致文件最后一位损坏，解压后少一位，弃用
import lzma
import requests
from lzma import LZMADecompressor
from lzma import LZMAError

def decompress_lzma(data):
    results = []
    while True:
        decomp = LZMADecompressor(lzma.FORMAT_AUTO, None, None)
        try:
            res = decomp.decompress(data)
        except LZMAError:
            if results:
                break  # Leftover data is not a valid LZMA/XZ stream; ignore it.
            else:
                raise  # Error on the first iteration; bail out.
        results.append(res)
        data = decomp.unused_data
        if not data:
            break
        if not decomp.eof:
            raise LZMAError("Compressed data ended before the end-of-stream marker was reached")
    return b"".join(results)

response = requests.get('http://content.warframe.com/PublicExport/index_zh.txt.lzma')
data = response.content
byt = bytes(data)
length = len(data)
stay = True
while stay:
    stay = False
    try:
        decompress_lzma(byt[0:length])
    except LZMAError:
        length -= 1
        stay = True

file_name = "api_content.txt"
file_content = open(f"content/{file_name}",'w')
file_content.write(decompress_lzma(byt[0:length]).decode('utf-8'))
file_content.close
print(decompress_lzma(byt[0:length]))