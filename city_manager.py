import json
import requests
from dotenv import load_dotenv
import os

class City:
    def __init__(self, name='Tokyo'):
        try:
            with open('errors.json', 'r') as file:
                self.request_errors_data = json.load(file)

        except FileNotFoundError:
            print('File not found')

        except json.decoder.JSONDecodeError:
            print('JSON decode error')

        load_dotenv()

        api_key = os.getenv('API_KEY')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={name}&appid={api_key}&units=metric'
        response = requests.get(url)

        if str(response.status_code) in self.request_errors_data.keys():
            self.error = response.status_code
            self.errorOccurred()

        else:
            self.error = None


            self.data = response.json()

            self.W_E_DATA = {
                'Thunderstorm': '🌩',
                'Drizzle': '🌦',
                'Rain': '🌧',
                'Snow': '🌨',
                'Clear': '👌',
                'Clouds': '☁',
            }


            self._name = name
            self._weather_emoji = self.W_E_DATA[self.data['weather'][0]['main']]
            self._temperature = int(self.data['main']['temp'])
            self._weather_description = self.data['weather'][0]['description']
            self._humidity = self.data['main']['humidity']
            self._pressure = self.data['main']['pressure']



    @property
    def name(self) -> str:
        return self._name

    @property
    def weather_emoji(self) -> str:
        return self._weather_emoji

    @property
    def weather_description(self) -> str:
        return self._weather_description + ','

    @property
    def temperature(self) -> str:
        return str(self._temperature) + '°C'

    @property
    def humidity(self) -> str:
        return str(self._humidity) + '%'

    @property
    def pressure(self) -> str:
        return str(self._pressure) + ' hPa'

    def errorOccurred(self) -> str:
        if self.error is None:
            return ''

        return self.request_errors_data[str(self.error)]

