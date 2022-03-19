################################################################################
# Scraping Single Wikipedia Page - Example 1.
################################################################################
# This page exctracts links from single wikipedia page in a simplistic way:
from urllib import request
from bs4 import BeautifulSoup as BS
import re
musicians_R_links = []
# Look at the page and the code
url = 'https://en.wikipedia.org/wiki/Lists_of_musicians' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find('span',id = 'R').parent.find_next_sibling('div').find_all('li')

links = ['http://en.wikipedia.org' + tag.a['href'] for tag in tags]

musicians_R_links.extend(links)

for link in musicians_R_links:
    print(link)