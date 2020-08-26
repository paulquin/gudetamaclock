from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from font_intuitive import Intuitive
import time
from inky import InkyPHAT
from datetime import datetime
from moonphase import *
from weather import *
from icon import *
from graphics import *
from concat import *

print("""Starting....""")

# Time

t = time.strftime('%H:%M ish...')

print(t)

# UTC Timestamp

utc = datetime.timestamp(datetime.now())

# Temperature

tempC = temperature()

# Daytime or Nighttime 

daytime = ''
utcsunrise = sunrise()
utcsunset = sunset()

# Determine moonphase

moonphaseid = int(float(moonphase()))
moonpath = moon_path()

print(tempC)

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

# Load the fonts

intuitive_font = ImageFont.truetype(Intuitive, int(23 * scale_size))
hanken_bold_font = ImageFont.truetype(HankenGroteskBold, int(16 * scale_size))


if utc >= utcsunrise and utc <= utcsunset: 
	for y in range(0, inky_display.HEIGHT):
		for x in range(0, x_half):
			img.putpixel((x, y), inky_display.WHITE)

	t_w, t_h = intuitive_font.getsize(t)
	t_x = int((x_half - t_w) / 2)
	t_y = int(y_half + ((y_half - t_h) /2))
	draw.text((t_x, t_y), t, inky_display.BLACK, font=intuitive_font)

	tempC_w, tempC_h = hanken_bold_font.getsize(tempC)
	tempC_x = int((61) + ((x_half - 61) - tempC_w)/2)
	tempC_y = int((y_half - tempC_h) /2)
	draw.text((tempC_x, tempC_y), tempC, inky_display.BLACK, font=hanken_bold_font)

else:
	for y in range(0, inky_display.HEIGHT):
		for x in range(0, x_half):
			img.putpixel((x, y), inky_display.BLACK)
	
	t_w, t_h = intuitive_font.getsize(t)
	t_x = int((x_half - t_w) / 2)
	t_y = int(y_half + ((y_half - t_h) /2))
	draw.text((t_x, t_y), t, inky_display.WHITE, font=intuitive_font)

	tempC_w, tempC_h = hanken_bold_font.getsize(tempC)
	tempC_x = int((61) + ((x_half - 61) - tempC_w)/2)
	tempC_y = int((y_half - tempC_h) /2)
	draw.text((tempC_x, tempC_y), tempC, inky_display.WHITE, font=hanken_bold_font)


### Concatenate two images

graphics = Image.open(graphics_path())

im = concat1(img, graphics)

icon = Image.open(icon_path())

finalimage = concat2(icon, im)

print("""Ready to display""")

# Display whatever 

inky_display.set_image(finalimage)
inky_display.show()
