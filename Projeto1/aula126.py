import requests
from bs4 import BeautifulSoup

url = 'https://g1.globo.com/mundo/noticia/2024/10/10/moradores-registram-tornados-em-diversas-partes-da-florida-video.ghtml'

response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

top_choices = parsed_html.select_one('body > div.glb-grid > main')
article = top_choices.parent
for p in article.select('p'):
    print(p)