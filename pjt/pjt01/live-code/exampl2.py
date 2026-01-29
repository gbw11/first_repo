import requests
from pprint import pprint

# "Tokyp, JP", "New York, US"
cityname = "seoul"
apikey = '8d635fde55f421e52d85dbf4476c0d7d'

lat = 0
lon = 0
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}'
response = requests.get(url).json()
pprint(response)