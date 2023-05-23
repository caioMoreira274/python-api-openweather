import requests
from pprint import pprint

class Geocoding:
    def __init__(self,nome_cidade):
        self.nome_cidade = nome_cidade
        self.pegar_lat_lon()

    def pegar_lat_lon(self):
        res = requests.get('http://api.openweathermap.org/geo/1.0/direct?q='+self.nome_cidade+'&appid=b125732752fad04c6ce7e29448cf95fd'
            ).json()
        self.lat = str(res[0]['lat'])
        self.lon = str(res[0]['lon'])


class ApiWeather:
    def __init__(self, geocoding):
        self.geo = geocoding
        self.dados = self.coletar_dados_cidade()

    def coletar_dados_cidade(self):
        res = requests.get(url=
            'https://api.openweathermap.org/data/2.5/weather?lat='+self.geo.lat+'&lon='+self.geo.lon+'&appid=b125732752fad04c6ce7e29448cf95fd&units=metric&lang=pt_br'
            ).json()
        return res

    def pegar_clima(self):
        return self.dados['weather'][0]['main'] +' '+ self.dados['weather'][0]['description']


geo = Geocoding('Bauru')
previsao_cidade = ApiWeather(geo)

pprint(previsao_cidade.pegar_clima())