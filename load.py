# %%
from Scrap import Scrap
import pandas as pd

# %%
data = Scrap('https://finance.yahoo.com/markets/stocks/most-active/')
df = pd.DataFrame(data.scrap_content_table())
df
# %%
