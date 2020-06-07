import requests
from bs4 import BeautifulSoup

URL =  "https://auto.ria.com/legkovie/jeep/"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36', 'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html,'html.parser')

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print(html.text)
    else:
        print('Error')



parse()
