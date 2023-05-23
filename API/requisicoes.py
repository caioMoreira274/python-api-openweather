import requests
from datetime import datetime, timedelta
from pprint import pprint

class Timezones:
    def __init__ (self):
        self.timezone_hours =   {"-43200":-12,"-39600":-11,"-3600":-10,"-34200":-9,"-32400":-9,"-28800":-8,"-25200":-7,"-21600":-6,"-18000":-5,"-16200":-4,"-14400":-4,"-12600":-3,"-10800":-3,"-7200":-2,"-3600":-1,"0":0,"50400":14,"46800":13,"45900":12,"43200":12,"41400":11,"39600":11,"3600":10,"34200":9,"32400":9,"28800":8,"25200":7,"21600":6,"18000":5,"16200":4,"14400":4,"12600":3,"10800":3,"7200":2,"3600":1}
        self.timezone_minutes = {"-43200":-00,"-39600":-00,"-3600":-00,"-34200":-30,"-32400":-00,"-28800":-00,"-25200":-00,"-21600":-00,"-18000":-00,"-16200":-30,"-14400":-00,"-12600":-30,"-10800":-00,"-7200":-00,"-3600":-00,"0":00,"50400":00,"46800":00,"45900":45,"43200":00,"41400":30,"39600":00,"36000":00,"34200":30,"32400":00,"28800":00,"25200":00,"21600":00,"18000":00,"16200":30,"14400":00,"12600":30,"10800":00,"7200":00,"3600":00}


class Sunrise_Sunset:    
    def __init__(self):
        self.hoje = str(datetime.now().date())
        self.dados = self.pegar_dados_sunrise_sunset()
        self.sunrise = self.dados['results']['sunrise']
        self.sunset = self.dados['results']['sunset']
        
        
    def pegar_dados_sunrise_sunset(self):
        res = requests.get(url='https://api.sunrise-sunset.org/json?lat='+geo.lat+'&lng='+geo.lon+'&date='+self.hoje
            ).json()    
        return  res     
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

    def pegar_timezone(self):
        return str(self.dados['timezone'])

    def pegar_tempo(self):
        print('\nTempo: ' + self.dados['weather'][0]['main'] + '\nDescrição: ' + self.dados['weather'][0]['description'])
    
    def pegar_dados_temperatura(self):
        print('\nTempreratura atual: ' + str(self.dados['main']['temp']) + '°C' + '\nSensação de: ' + str(self.dados['main']['feels_like']) + '°C' + '\nTemperatura máxima: ' + str(self.dados['main']['temp_max']) + '°C' + '\nTemperatura mínima: ' + str(self.dados['main']['temp_min']) + '°C')
    
    def pegar_humidade(self):
        print('\nHumidade relativa em ' + str(self.dados['main']['humidity']) + '%')
    
    def pegar_dados_nascer_do_sol(self):            

        nascer_do_sol_utc0 = sun.sunrise
        nascer_do_sol_datetime = datetime.strptime(nascer_do_sol_utc0, "%I:%M:%S %p")
        nascer_do_sol_utc3 = nascer_do_sol_datetime - timedelta(hours=3)
        nascer_do_sol_utc3 = nascer_do_sol_datetime + timedelta(hours=-3)

        nascer_do_sol_utc3_str = nascer_do_sol_utc3.strftime("%I:%M:%S %p")

        print('\nNascer do sol hoje ' + nascer_do_sol_utc3_str)
                
    def pegar_dados_por_do_sol(self):
        nascer_do_sol_utc0 = sun.sunset
        nascer_do_sol_datetime = datetime.strptime(nascer_do_sol_utc0, "%I:%M:%S %p")
        nascer_do_sol_utc3 = nascer_do_sol_datetime - timedelta(hours=3)
        nascer_do_sol_utc3 = nascer_do_sol_datetime + timedelta(hours=-3)

        nascer_do_sol_utc3_str = nascer_do_sol_utc3.strftime("%I:%M:%S %p")

        print('\nPôr do sol hoje ' + nascer_do_sol_utc3_str)




geo = Geocoding('Bauru')
previsao_cidade = ApiWeather(geo)
sun = Sunrise_Sunset()



previsao_cidade.pegar_tempo() 
previsao_cidade.pegar_dados_temperatura()
previsao_cidade.pegar_dados_nascer_do_sol()
previsao_cidade.pegar_dados_por_do_sol()
previsao_cidade.pegar_humidade()
#previsao_cidade.pegar_tempo() 
#previsao_cidade.pegar_dados_temperatura()
#previsao_cidade.pegar_humidade()
#previsao_cidade.pegar_dados_nascer_do_sol()
#previsao_cidade.pegar_dados_por_do_sol()
print(previsao_cidade.pegar_timezone())