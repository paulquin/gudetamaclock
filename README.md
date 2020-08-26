# gudetamaclock

A Gudetama-themed clock displayed on raspberry pi zero w with a inky phat display

Not only it has different Gudetamas for different time, it shows weather, temperature and moonphase (when the sky is clear during nights.)

To customize your location, change [weather.py](https://github.com/paulquin/gudetamaclock/blob/master/weather.py) and [moonphase.py](https://github.com/paulquin/gudetamaclock/blob/master/moonphase.py) with respect to your location

I recommend adjusting the "special days" in [graphics.py](graphics.py) as not everyone has the same birthday

Weather is obtained through [OpenWeather API](https://openweathermap.org/current) and requires your own API key in order to make the [weather.py](https://github.com/paulquin/gudetamaclock/blob/master/weather.py) works.

Moonphase is obtained through [Meteorologisk institutt](https://www.met.no/) of their [Sunrise](https://api.met.no/weatherapi/sunrise/2.0/documentation) API, which does not require any API key.
