from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ApplewebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537 .3'}

def weather(city):
    city = city.replace(' ', '+')
    print('Searching...')

    res = requests.get(f'https://www.google.com/search?q={city}', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    if 'wob_loc' in soup == 0:
        print('Enter the REAL city or postal code')
    else:
        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        celsius = soup.select('#wob_tm')[0].getText().strip()
        fahrenheit = soup.select('#wob_ttm')[0].getText().strip()
        rain = soup.select('#wob_pp')[0].getText().strip()
        humidity = soup.select('#wob_hm')[0].getText().strip()
        wind = soup.select('#wob_ws')[0].getText().strip()

        print()
        print('City:', location)
        print('Time:', time)
        print('Weather conditions:', info) #состояние погоды
        print('Temperature:', celsius + '°C' + ' / ' + fahrenheit + '°F')
        print('Rain:', rain) 
        print('Humidity:', humidity)
        print('Wind:', wind)
        print()


print()
city = input ('Enter your City or Postal/ZIP Code: ')
city = city + '+weather'
weather(city)