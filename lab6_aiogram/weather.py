import requests

app_id = "0d6eb8362cfe0622d5bc1b40279fb037"


def test(name):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': name, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
        data = res.json()['list'][0]
    except:
        return False
    return True if data is not None else False


class Weather:
    def __init__(self):
        self._city = ""
        self._country = ""
        self._app_id = app_id

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    def get_weather(self):
        place = ''.join([self.city, ', ', self.country])

        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/find",
                               params={'q': place, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
            data = res.json()['list'][0]

            city = data['name'] + ' ' + str(data['sys']['country'])
            cond = "Условия:" + ' ' + data['weather'][0]['description']
            temp = "Температура:" + ' ' + str(data['main']['temp'])
            temp_min = "Минимальная температура:" + ' ' + str(data['main']['temp_min'])
            temp_max = "Максимальная температура:" + ' ' + str(data['main']['temp_max'])
            feels_like = "Ощущается как:" + ' ' + str(data['main']['feels_like'])
            response = ''.join(
                [city + '\n', cond + '\n', temp + '\n', feels_like + '\n', temp_min + '\n', temp_max + '\n', ])
            return response
        except Exception as e:
            print("Exception (weather):", e)
            pass


if __name__ == '__main__':
    w = Weather()
    w.city = 'ASF'
    # w.country = 'Россия'
    # w.get_weather()
    print(w.test())
