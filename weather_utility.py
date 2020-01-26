#!/usr/bin/python

from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather
from darksky.forecast import Forecast 
from geopy.geocoders import Nominatim

class WeatherUtility:

    API_KEY = '9eb2c367bb175398754ac86f4f47a6b9'

    darksky = DarkSky(API_KEY)

    geolocator = Nominatim(user_agent = "The Music Forecast")
    input_loc = input("Enter your city: ")
    location = geolocator.geocode(input_loc)
    print(location.address)
    if location.address[-24:] == 'United States of America':
        print("yes")
    print((location.latitude, location.longitude))

    latitude = location.latitude
    longitude = location.longitude

    #latitude = 35.8486
    #longitude = -86.2649

    forecast = darksky.get_forecast(
        latitude, longitude,
        extend=False, # default `False`
        lang=languages.ENGLISH, # default `ENGLISH`
        units=units.AUTO, # default `auto`
        exclude=[weather.MINUTELY, weather.ALERTS], # default `[]`,
    )

    time = forecast.currently.time
    precip_intensity = forecast.currently.precip_intensity
    precip_type = forecast.currently.precip_type
    temp = forecast.currently.temperature
    wind_speed = forecast.currently.wind_speed
    cloud_cover = forecast.currently.cloud_cover
    visibility = forecast.currently.visibility

    print(time)
    print(precip_intensity)
    print(precip_type)
    print(temp)
    print(wind_speed)
    print(cloud_cover)
    print(visibility)

    def BPM(temp, wind_speed, intensity, time):
        temp_wght = 0.15
        wind_spd_wght = 0.35
        intensity_wght = 0.4 
        time_wght = 0.1

        

