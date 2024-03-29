import requests

lat = 12.2
lon = 13.7
apiKey = '1bf779b770c0a107b0cce8a6eec0f09c'

try:
    city=input('Enter a city: ')

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={apiKey}'

    response = requests.get(url.format(city)).json() 
    
    print(response)

except requests.RequestException as e:
    print("Request failed:", e)