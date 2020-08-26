from weather import *
from moonphase import *
from datetime import datetime

weatherid = wid()
utcsunrise = sunrise()
utcsunset = sunset()
utc = datetime.timestamp(datetime.now())
moonpath = moon_path()

def icon_path():

	if utc >= utcsunrise and utc <= utcsunset:
		if weatherid >= 200 and weatherid < 299:
			iconpath = "/home/pi/clock/GudeClock/icon/thunder1.png"
		elif weatherid >= 300 and weatherid < 399:
			iconpath = "/home/pi/clock/GudeClock/icon/drizzle1.png"
		elif weatherid >= 500 and weatherid < 599:
			iconpath = "/home/pi/clock/GudeClock/icon/rain1.png"
		elif weatherid >= 600 and weatherid < 699:
			iconpath = "/home/pi/clock/GudeClock/icon/snow1.png"
		elif weatherid >= 700 and weatherid < 799:
			iconpath = "/home/pi/clock/GudeClock/icon/mist1.png"
		elif weatherid == 800:
			iconpath = "/home/pi/clock/GudeClock/icon/clear1.png"
		elif weatherid == 801 or weatherid == 802:
			iconpath = "/home/pi/clock/GudeClock/icon/pcloud1.png"
		elif weatherid == 803 or weatherid == 804:
			iconpath = "/home/pi/clock/GudeClock/icon/cloud1.png"
		else:
			iconpath = "/home/pi/clock/GudeClock/icon/1.png"
	else:
		if weatherid >= 200 and weatherid < 299:
			iconpath = "/home/pi/clock/GudeClock/icon/thunder2.png"
		elif weatherid >= 300 and weatherid < 399:
			iconpath = "/home/pi/clock/GudeClock/icon/drizzle2.png"
		elif weatherid >= 500 and weatherid < 599:
			iconpath = "/home/pi/clock/GudeClock/icon/rain2.png"
		elif weatherid >= 600 and weatherid < 699:
			iconpath = "/home/pi/clock/GudeClock/icon/snow2.png"
		elif weatherid >= 700 and weatherid < 799:
			iconpath = "/home/pi/clock/GudeClock/icon/mist2.png"
		elif weatherid == 800:
			iconpath = moonpath
		elif weatherid == 801 or weatherid == 802:
			iconpath = "/home/pi/clock/GudeClock/icon/pcloud2.png"
		elif weatherid == 803 or weatherid == 804:
			iconpath = "/home/pi/clock/GudeClock/icon/cloud2.png"
		else:
			iconpath = "/home/pi/clock/GudeClock/icon/2.png"
		
	return iconpath
