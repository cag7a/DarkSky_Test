from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather

API_KEY = '9eb2c367bb175398754ac86f4f47a6b9'

darksky = DarkSky(API_KEY)

latitude = 42.3601
longitude = -71.0589

forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    units=units.AUTO, # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS], # default `[]`,
    timezone='UTC' # default None - will be set by DarkSky API automatically
)

