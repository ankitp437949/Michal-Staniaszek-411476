################################################################################
# Scraping Single Wikipedia Page - Example 1.
################################################################################
# This page exctracts links from single wikipedia page in a simplistic way:
from urllib import request
from bs4 import BeautifulSoup as BS
import re

# Look at the page and the code
url = 'https://en.wikipedia.org/wiki/List_of_painters_by_name' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find_all('a', {'title':re.compile('List of painters.*')})

links = ['http://en.wikipedia.org' + tags]

for link in links:
    print(link)