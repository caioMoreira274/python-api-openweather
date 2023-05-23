import requests
from datetime import datetime, timedelta
from pprint import pprint

#      Classe Sunrise_Sunset usa a API: 'https://api.sunrise-sunset.org', que mostra nascer e por do sol para o usuário de forma legível, \\
#    já a API OpenWeatherMap é muito diferente do usual e mostra números que não são muito diferentes para o usuário 

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
@@ -24,11 +43,54 @@ def coletar_dados_cidade(self):
            ).json()
        return res

    def pegar_clima(self):
        return self.dados['weather'][0]['main'] +' '+ self.dados['weather'][0]['description']
    def pegar_tempo(self):
        print('TEMPO''\nTempo: ' + self.dados['weather'][0]['main'] + '\nDescrição: ' + self.dados['weather'][0]['description'] + '\n\n')

    def pegar_dados_temperatura(self):
        print('TEMPERATURA''\nTempreratura atual: ' + str(self.dados['main']['temp']) + '°C' + '\nSensação de: ' + str(self.dados['main']['feels_like']) + '°C' + '\n   Temperatura máxima: ' + str(self.dados['main']['temp_max']) + '°C' + '\n   Temperatura mínima: ' + str(self.dados['main']['temp_min']) + '°C' + '\n\n')

    def pegar_humidade(self):
        print('Humidade relativa em: ' + str(self.dados['main']['humidity']) + '%')

    def pegar_dados_nascer_do_sol(self):            


        nascer_do_sol_utc0 = sun.sunrise
        nascer_do_sol_datetime = datetime.strptime(nascer_do_sol_utc0, "%I:%M:%S %p")
        nascer_do_sol_utc3 = nascer_do_sol_datetime - timedelta(hours=3)
        nascer_do_sol_utc3_str = nascer_do_sol_utc3.strftime("%I:%M:%S %p")

        print('Nascer do sol hoje: ' + nascer_do_sol_utc3_str)

    def pegar_dados_por_do_sol(self):

        nascer_do_sol_utc0 = sun.sunset
        nascer_do_sol_datetime = datetime.strptime(nascer_do_sol_utc0, "%I:%M:%S %p")
        nascer_do_sol_utc3 = nascer_do_sol_datetime - timedelta(hours=3)
        nascer_do_sol_utc3_str = nascer_do_sol_utc3.strftime("%I:%M:%S %p")

        print('Pôr do sol hoje: ' + nascer_do_sol_utc3_str)


geo = Geocoding('Bauru')
previsao_cidade = ApiWeather(geo)
sun = Sunrise_Sunset()



pprint(previsao_cidade.pegar_clima())
#previsao_cidade.pegar_tempo()
#previsao_cidade.pegar_dados_temperatura()
#previsao_cidade.pegar_dados_nascer_por_do_sol()
#previsao_cidade.pegar_dados_nascer_do_sol()
#previsao_cidade.pegar_dados_por_do_sol()
previsao_cidade.pegar_humidade()