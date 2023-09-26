from PIL import Image,ImageDraw,ImageFont,ImageFilter
import requests
 
api=requests.get("http://nymph.rbq.life:3000/wm/robot/摸")
text=api.text

# PIL实现
width=616
height=610
im=Image.new('RGB',(width,height),(255,255,255))
dr=ImageDraw.Draw(im)
font=ImageFont.truetype("render/msyh.ttc",25)
dr.text((5,5),text,font=font,fill='#0000FF')
im.save("render/t.png")