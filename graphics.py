import time
from weather import *

year = int(time.strftime('%Y'))
weekday = int(time.strftime('%w'))
day = str(time.strftime('%m%d'))
hour = int(time.strftime('%H'))
weatherid = wid()

def graphics_path():

	if hour == 1:
		graphicspath = "/home/pi/clock/GudeClock/graphics/eggshausted.png"
	elif hour == 2:
		graphicspath = "/home/pi/clock/GudeClock/graphics/bed.png"
	elif hour == 3:
		graphicspath = "/home/pi/clock/GudeClock/graphics/ahhh.png"
	elif hour >= 4 and hour <= 6:
		graphicspath = "/home/pi/clock/GudeClock/graphics/depressed.png"
	elif hour == 7:
		graphicspath = "/home/pi/clock/GudeClock/graphics/shy.png"
	elif hour == 8:
		graphicspath = "/home/pi/clock/GudeClock/graphics/tumble.png"
	elif hour == 9:
		graphicspath = "/home/pi/clock/GudeClock/graphics/tired.png"
	elif hour == 10:
		graphicspath = "/home/pi/clock/GudeClock/graphics/what.png"
	elif hour == 11:
		graphicspath = "/home/pi/clock/GudeClock/graphics/laidback.png"
	elif hour == 12:
		graphicspath = "/home/pi/clock/GudeClock/graphics/reverse.png"
	elif hour == 13:
		graphicspath = "/home/pi/clock/GudeClock/graphics/shell.png"
	elif hour == 14:
		graphicspath = "/home/pi/clock/GudeClock/graphics/flower.png"
	elif hour == 15:
		graphicspath = "/home/pi/clock/GudeClock/graphics/chill.png"
	elif hour == 16:
		graphicspath = "/home/pi/clock/GudeClock/graphics/zzz.png"
	elif hour == 17:
		graphicspath = "/home/pi/clock/GudeClock/graphics/dozing.png"
	elif hour == 18:
		graphicspath = "/home/pi/clock/GudeClock/graphics/meh.png"
	elif hour == 19:
		graphicspath = "/home/pi/clock/GudeClock/graphics/whatever.png"
	elif hour == 20:
		graphicspath = "/home/pi/clock/GudeClock/graphics/wa.png"
	elif hour == 21:
		graphicspath = "/home/pi/clock/GudeClock/graphics/hood.png"
	elif hour == 22:
		graphicspath = "/home/pi/clock/GudeClock/graphics/stuck.png"
	elif hour == 23:
		graphicspath = "/home/pi/clock/GudeClock/graphics/handstand.png"	

	else:
		graphicspath = "/home/pi/clock/GudeClock/graphics/icon.png"

# Weekday

	if weekday == 5 and hour > 14 and hour <= 17:
		graphicspath = "/home/pi/clock/GudeClock/graphics/friday.png"
	else:
		graphicspath = graphicspath
	
# Weathers	

	if weatherid >= 502 and weatherid <= 504:
		graphicspath = "/home/pi/clock/GudeClock/graphics/brolly.png"
	elif weatherid == 602 or weatherid == 622:
		graphicspath = "/home/pi/clock/GudeClock/graphics/snow.png"
	elif weatherid == 804:
		graphicspath = "/home/pi/clock/GudeClock/graphics/meringue.png"
	else:
		graphicspath = graphicspath
	
# Special days

	if day == '0101':
		graphicspath = "/home/pi/clock/GudeClock/graphics/ballons.png"
	elif day == '0214':
		graphicspath = "/home/pi/clock/GudeClock/graphics/valentine.png"
	elif day == '0405' and year == 2021:
		graphicspath = "/home/pi/clock/GudeClock/graphics/bunny.png"
	elif day == '0418' and year == 2022:
		graphicspath = "/home/pi/clock/GudeClock/graphics/bunny.png"
	elif day == '0410' and year == 2023:
		graphicspath = "/home/pi/clock/GudeClock/graphics/bunny.png"
	elif day == '0829' and hour <= 10:
		graphicspath = "/home/pi/clock/GudeClock/graphics/valentine.png"
	elif day == '0829' and hour > 10 and hour <= 11 :
		graphicspath = "/home/pi/clock/GudeClock/graphics/bun.png"
	elif day == '0829' and hour > 11 and hour <= 12 :
		graphicspath = "/home/pi/clock/GudeClock/graphics/holdhands.png"
	elif day == '0829' and hour > 12 and hour <= 13 :
		graphicspath = "/home/pi/clock/GudeClock/graphics/twin.png"
	elif day == '1031' and hour > 12 and hour <= 14:
		graphicspath = "/home/pi/clock/GudeClock/graphics/xray.png"
	elif day == '1031' and hour > 14 and hour <= 16:
		graphicspath = "/home/pi/clock/GudeClock/graphics/boo.png"
	elif day == '1031' and hour > 16 and hour <= 18:
		graphicspath = "/home/pi/clock/GudeClock/graphics/halloween.png"
	elif day == '1031' and hour > 18 and hour <= 20:
		graphicspath = "/home/pi/clock/GudeClock/graphics/fairy.png"
	elif day == '1031' and hour > 20:
		graphicspath = "/home/pi/clock/GudeClock/graphics/jackolantern.png"
	elif day == '1225':
		graphicspath = "/home/pi/clock/GudeClock/graphics/christmas.png"
	elif day == '1231':
		graphicspath = "/home/pi/clock/GudeClock/graphics/birthday.png"
	else:
		graphicspath = graphicspath
	
	return graphicspath
