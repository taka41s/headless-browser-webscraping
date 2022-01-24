import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import json


url = 'https://finance.yahoo.com/quote/BTC-EUR/history?p=BTC-EUR'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(10)

driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]').click()
element = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table')
html_content = element.get_attribute('outerHTML')


soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

df_full=pd.read_html(str(table))[0].head(10)
df = df_full[['Date', 'Open', 'High', 'Low', 'Close*']]

converter = {}
converter['dict'] = df.to_dict('records')

driver.quit()


with open('eur-btc-rates.json', 'w') as write_file:
    json.dump(converter, write_file)
















