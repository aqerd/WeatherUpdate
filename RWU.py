from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ApplewebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537 .3'}

def weather(city):
    city=city.replace(' ', '+')
    res = requests.get(f'https://www.google.com/search?q={city}', headers=headers)
    print('Searching')
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather + '°C')

city = input ('Enter your City or Postal/ZIP Code: ')
city = city + '+weather'
weather(city)