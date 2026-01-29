import requests
from pprint import pprint

# 서울 위경도
lat = 37.56
lon = 126.97
apikey = '8d635fde55f421e52d85dbf4476c0d7d'

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}'
response = requests.get(url).json()
pprint(response)