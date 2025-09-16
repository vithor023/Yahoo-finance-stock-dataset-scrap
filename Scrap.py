# %%
from bs4 import BeautifulSoup
import requests

class Scrap:

    def __init__(self, url):
        self.url = url

    def request_url(self):
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) "
                "Gecko/20100101 Firefox/117.0"
            )
        }
        return requests.get(self.url, headers=headers).text

    def scrap_table(self):

        soup = BeautifulSoup(self.request_url(), 'html.parser').find('table',class_='yf-1m4mc7b bd')

        return soup

        


# %%
teste = Scrap('https://finance.yahoo.com/markets/stocks/most-active/')
teste.scrap_table()
# %%
