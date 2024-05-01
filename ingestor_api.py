import requests
import pandas as pd
import json
from datetime import date

#Parametros de consulta
#symbol = 'PBR'  #Symbol da ação sugerida  PBR -> Pétroleo Brasileiro S.A - Petrobras (PBR)
#outputsize = 'full' #full: tudo, compact: 100 dias
#apikey = '8023BW716Z4D4N2Q' #KEY DA API gratis

class GetInformation:
    def __init__(self,symbol,outputsize,apikey):
        self.symbol = symbol
        self.outputsize = outputsize
        self.apikey = apikey
    
    def get_file(self):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.symbol}&outputsize={self.outputsize}&apikey={self.apikey}'
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            # Modelando o dataset
            time_series = pd.DataFrame()
            time_series = time_series.from_dict(data['Time Series (Daily)'], orient='index')
            time_series = time_series.rename(columns = {'1. open':'open', '2. high':'high','3. low':'low','4. close':'close','5. volume':'volume'})
            time_series.index = pd.to_datetime(time_series.index)
            
            #Convertendo as colunas para numeric
            for column in time_series.columns:
                time_series[column] = pd.to_numeric(time_series[column])
        
            # Renomeando o index e ordenando index
            time_series.sort_index(inplace=True)
            time_series.index.rename('data', inplace=True)
            
            # Salvando a consulta em csv
            time_series.to_csv(f'time_series_{self.symbol}_{date.today()}.csv')
            return time_series
        else:
            print(f'Erro ao obter dados: {r.status_code}')