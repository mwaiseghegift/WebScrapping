from bs4 import BeautifulSoup

import requests


html_text = requests.get('https://www.kilimall.co.ke/new/commoditysearch?c=1072&aside=&gc_id=1072').text
soup = BeautifulSoup(html_text, 'lxml')
