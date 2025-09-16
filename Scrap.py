from datetime import datetime
from bs4 import BeautifulSoup
import requests

class Scrap:

    def __init__(self, url, params=None):
        self.url = url
        self.params = params
        
    def request_url(self):
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) "
                "Gecko/20100101 Firefox/117.0"
            )
        }
        return requests.get(self.url, headers=headers, params=self.params,).text

    def scrap_table(self):

        soup = BeautifulSoup(self.request_url(), 'html.parser').find('table',class_='yf-1m4mc7b bd')

        return soup

    def scrap_content_table(self):

        contents = []

        rows = self.scrap_table().find_all('tr', class_='row yf-1m4mc7b')
        for row in rows:
            lin = {}
            lin['company_name'] = row.find('td',{"data-testid-cell" : "companyshortname.raw"}).div.text
            lin['price'] = float(row.find('fin-streamer', {"data-field" :"regularMarketPrice"}).text)
            lin['change'] = float(row.find('fin-streamer', {"data-field" :"regularMarketChange"}).text)
            lin['change_percent (%)'] = row.find('fin-streamer', {"data-field" : "regularMarketChangePercent"}).text
            lin['volume (M)'] = float(row.find('fin-streamer',{"data-field" :"regularMarketVolume"}).text.replace('M',''))
            lin['AVG vol(3M)'] = float(row.find('td', {"data-testid-cell": "avgdailyvol3m"}).text.replace('M',''))
            lin['market_cap'] = row.find('fin-streamer',{"data-field" :"marketCap"}).text
            lin['P/E_ratio(TTM)'] = row.find('td', {"data-testid-cell" : "peratio.lasttwelvemonths"}).text
            lin['52_wk_change(%)'] = row.find('fin-streamer', {"data-field" :"fiftyTwoWeekChangePercent"}).text
            lin['date'] = datetime.today().strftime('%Y-%m-%d')
            contents.append(lin)
        
        return contents


