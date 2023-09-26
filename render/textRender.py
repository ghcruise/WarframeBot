from PIL import Image,ImageDraw,ImageFont,ImageFilter
import requests
text="text\ntest\n测试"
 
api=requests.get("http://nymph.rbq.life:3000/wm/robot/摸")
text=api.text

# PIL实现
width=100*8
height=100*4
im=Image.new('RGB',(width,height),(255,255,255))
dr=ImageDraw.Draw(im)
font=ImageFont.truetype("render/msyh.ttc",20)
dr.text((10,5),text,font=font,fill='#000000')
im.save("render/t.png")