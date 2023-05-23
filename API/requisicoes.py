import requests
from datetime import datetime, timedelta
from pprint import pprint

class Timezones:
    def __init__ (self):
        self.timezone_hours = {"-43200":-12,"-39600":-11,"-3600":-10,"-34200":-9,"-32400":-9,"-28800":-8,"-25200":-7,"-21600":-6,
                                 "-18000":-5,"-16200":-4,"-14400":-4,"-12600":-3,"-10800":-3,"-7200":-2,"-3600":-1,"0":0,"50400":14,
                                 "46800":13,"45900":12,"43200":12,"41400":11,"39600":11,"3600":10,"34200":9,"32400":9,"28800":8,
                                 "25200":7,"21600":6,"18000":5,"16200":4,"14400":4,"12600":3,"10800":3,"7200":2,"3600":1}

        self.timezone_minutes = {"-43200":-00,"-39600":-00,"-3600":-00,"-34200":-30,"-32400":-00,"-28800":-00,"-25200":-00,"-21600":-00,
                                 "-18000":-00,"-16200":-30,"-14400":-00,"-12600":-30,"-10800":-00,"-7200":-00,"-3600":-00,"0":00,"50400":00,
                                 "46800":00,"45900":45,"43200":00,"41400":30,"39600":00,"36000":00,"34200":30,"32400":00,"28800":00,
                                 "25200":00,"21600":00,"18000":00,"16200":30,"14400":00,"12600":30,"10800":00,"7200":00,"3600":00}

        self.code = str(previsao_cidade.dados['timezone'])
        self.hora = self.horas_identificada()
        self.minuto = self.minutos_identificados()
    def horas_identificada(self):
        if self.code in self.timezone_hours:
            valor_correspondente = self.timezone_hours[self.code]
            return valor_correspondente
        else:
            print("Valor externo não encontrado no dicionário")
    def minutos_identificados(self):
        if self.code in self.timezone_minutes:
            valor_correspondente = self.timezone_minutes[self.code]
            return valor_correspondente
        else:
            print("Valor externo não encontrado no dicionário")

   
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
        self.tempo_main = self.pegar_tempo_main()

    def coletar_dados_cidade(self):
        res = requests.get(url=
            'https://api.openweathermap.org/data/2.5/weather?lat='+self.geo.lat+'&lon='+self.geo.lon+'&appid=b125732752fad04c6ce7e29448cf95fd&units=metric&lang=pt_br'
            ).json()
        return res

    def pegar_timezone(self):
        return str(self.dados['timezone'])

    def pegar_tempo_main(self):
        return self.dados['weather'][0]['main']

    def pegar_tempo(self):
        print('\nTempo: ' + trad.texto_traduzido + '\nDescrição: ' + self.dados['weather'][0]['description'])

    def pegar_dados_temperatura(self):
        print('\nTempreratura atual: ' + str(self.dados['main']['temp']) + '°C' + '\nSensação de: ' + str(self.dados['main']['feels_like']) + '°C' + '\nTemperatura máxima: ' + str(self.dados['main']['temp_max']) + '°C' + '\nTemperatura mínima: ' + str(self.dados['main']['temp_min']) + '°C')
    
    def pegar_humidade(self):
        print('\nHumidade relativa em ' + str(self.dados['main']['humidity']) + '%')

    def pegar_dados_nascer_do_sol(self):            

        nascer_do_sol_utc0 = sun.sunrise
        nascer_do_sol_datetime = datetime.strptime(nascer_do_sol_utc0, "%I:%M:%S %p")
        nascer_do_sol_utc3 = nascer_do_sol_datetime + timedelta(hours=time.hora)
        nascer_do_sol_utc = nascer_do_sol_utc3 + timedelta(minutes=time.minuto)
        
        nascer_do_sol_utc3_str = nascer_do_sol_utc.strftime("%I:%M:%S %p")
        print('\nNascer do sol hoje ' + nascer_do_sol_utc3_str)
                
    def pegar_dados_por_do_sol(self):
        por_do_sol_utc0 = sun.sunset
        por_do_sol_datetime = datetime.strptime(por_do_sol_utc0, "%I:%M:%S %p")
        por_do_sol_utc3 = por_do_sol_datetime + timedelta(hours=time.hora)
        por_do_sol_utc = por_do_sol_utc3 + timedelta(minutes=time.hora)
        por_do_sol_utc = por_do_sol_utc3 + timedelta(minutes=time.minuto)

        por_do_sol_utc3_str = por_do_sol_utc.strftime("%I:%M:%S %p")

        print('\nPôr do sol hoje ' + por_do_sol_utc3_str)

# Classe Tradutor usada no método pegar_tempo() da classe ApiWeather pois a API não fornece a informação em português, mesmo com o parâmetro especificado para pt_br
class Tradutor:
    def __init__(self,texto):
        self.texto = texto
        self.texto_traduzido = self.traduzido()

    def traduzido(self):
        api_url = f"https://api.mymemory.translated.net/get?q=Weather%20{self.texto}&langpair=en|pt"
        response = requests.get(api_url)
        response_dict = response.json()
        translated_text = response_dict['responseData']['translatedText']
        return translated_text


cidade_desejada = input('Escreva o nome de uma cidade: ')

geo = Geocoding(cidade_desejada)
previsao_cidade = ApiWeather(geo)
sun = Sunrise_Sunset()
time = Timezones()
trad = Tradutor(texto=previsao_cidade.tempo_main)



previsao_cidade.pegar_tempo() 
previsao_cidade.pegar_dados_temperatura()
previsao_cidade.pegar_humidade()
previsao_cidade.pegar_dados_nascer_do_sol()
previsao_cidade.pegar_dados_por_do_sol()
#print(previsao_cidade.pegar_timezone())
