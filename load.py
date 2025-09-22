from Scrap import Scrap
from sqlalchemy import create_engine
import pandas as pd

database_url = "postgresql+psycopg2://root:root@192.168.100.139:5432/yahoofinance"
engine = create_engine(database_url)

list_url = ['https://finance.yahoo.com/markets/stocks/most-active/']

for url in list_url:
    scrap = Scrap(url)
    data_content = scrap.scrap_content_table()
    df = pd.DataFrame(data_content)
    df.to_sql('actives_treanding', con=engine, if_exists='append', index=False)
    print('dados inseridos com sucesso!')

