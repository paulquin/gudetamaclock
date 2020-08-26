import time
import requests

def moonphase():
	url = 'https://api.met.no/weatherapi/sunrise/2.0/.json?'

	lat = '49.283054'
	lon = '-122.831665'
	date = time.strftime('%Y-%m-%d')
	offset = '-07:00'

	query = 'lat={}&lon={}&date={}&offset={}'.format(lat,lon,date,offset)

	request = url + query
	result = requests.get(request)
	data = result.json()

	moonphaseid = data['location']['time'][0]['moonphase']['value']
	
	return moonphaseid

def moon_path():
	moonphaseid = int(float(moonphase()))

	if moonphaseid == 0:
		moonpath = "/home/pi/clock/GudeClock/icon/m0.png"
	elif moonphaseid > 0 and moonphaseid <= 6:
		moonpath = "/home/pi/clock/GudeClock/icon/m6.png"
	elif moonphaseid > 6 and moonphaseid <= 12:
		moonpath = "/home/pi/clock/GudeClock/icon/m12.png"
	elif moonphaseid > 12 and moonphaseid <= 18:
		moonpath = "/home/pi/clock/GudeClock/icon/m12.png"
	elif moonphaseid > 18 and moonphaseid <= 25:
		moonpath = "/home/pi/clock/GudeClock/icon/m18.png"
	elif moonphaseid > 25 and moonphaseid <= 31:
		moonpath = "/home/pi/clock/GudeClock/icon/m25.png"
	elif moonphaseid > 31 and moonphaseid <= 37:
		moonpath = "/home/pi/clock/GudeClock/icon/m31.png"
	elif moonphaseid > 37 and moonphaseid <= 43:
		moonpath = "/home/pi/clock/GudeClock/icon/m37.png"
	elif moonphaseid > 43 and moonphaseid <= 50:
		moonpath = "/home/pi/clock/GudeClock/icon/m43.png"
	elif moonphaseid > 50 and moonphaseid <= 56:
		moonpath = "/home/pi/clock/GudeClock/icon/m50.png"	
	elif moonphaseid > 56 and moonphaseid <= 62:
		moonpath = "/home/pi/clock/GudeClock/icon/m56.png"	
	elif moonphaseid > 62 and moonphaseid <= 68:
		moonpath = "/home/pi/clock/GudeClock/icon/m62.png"	
	elif moonphaseid > 68 and moonphaseid <= 75:
		moonpath = "/home/pi/clock/GudeClock/icon/m68.png"	
	elif moonphaseid > 75 and moonphaseid <= 81:
		moonpath = "/home/pi/clock/GudeClock/icon/m75.png"	
	elif moonphaseid > 81 and moonphaseid <= 87:
		moonpath = "/home/pi/clock/GudeClock/icon/m81.png"
	elif moonphaseid > 87 and moonphaseid <= 93:
		moonpath = "/home/pi/clock/GudeClock/icon/m87.png"
	elif moonphaseid > 93 and moonphaseid < 100:
		moonpath = "/home/pi/clock/GudeClock/icon/m93.png"
	else:
		moonpath = "/home/pi/clock/GudeClock/icon/m100.png"
	return moonpath
