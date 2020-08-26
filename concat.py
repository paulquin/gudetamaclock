from PIL import Image, ImageFont, ImageDraw
from inky import InkyPHAT
from inky.auto import auto

inky_display = auto()
x_half = int(inky_display.WIDTH / 2)
y_half = int(inky_display.HEIGHT / 2)

def concat1(img_L,img_R):
	im = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
	im.paste(img_L, (0,0))
	im.paste(img_R, (x_half, 0))
	return im

def concat2(w_icon, main):
	im = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
	im.paste(main, (0,0))
	im.paste(w_icon, (0, 0))
	return im
