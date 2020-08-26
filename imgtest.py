from PIL import Image, ImageFont, ImageDraw

from inky import InkyPHAT

print("Starting image testing...")

# Set display

from inky.auto import auto

inky_display = auto()
scale_size = 1
padding = 0

colour = inky_display.colour

x_half = int(inky_display.WIDTH / 2)
y_half = int(inky_display.HEIGHT / 2)


# inky_display.set_rotation(180)

inky_display.set_border(inky_display.YELLOW)

# Create canvas

img = Image.new("P", (x_half, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

imgpath1 = "/home/pi/clock/GudeClock/graphics/break.png"
imgpath2 = "/home/pi/clock/GudeClock/graphics/tired.png"

print("Image to be displayed: " + imgpath1)
print("Image to be displayed: " + imgpath2)

img1 = Image.open(imgpath1)
img2 = Image.open(imgpath2)

def concat1(img_1,img_2):
	im = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
	im.paste(img_1, (0,0))
	im.paste(img_2, (x_half, 0))
	return im

combinedimage = concat1(img1, img2)

print("""Ready to display""")

# Display whatever 

inky_display.set_image(combinedimage)
inky_display.show()
