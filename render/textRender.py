from PIL import Image,ImageDraw,ImageFont,ImageFilter
 
text="text\ntest\n测试"
 
 
# PIL实现
width=60*4
height=60*2
im=Image.new('RGB',(width,height),(255,255,255))
dr=ImageDraw.Draw(im)
font=ImageFont.truetype("render/msyh.ttc",20)
dr.text((10,5),text,font=font,fill='#000000')
im.save("render/t.png")