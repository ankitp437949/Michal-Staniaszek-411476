#############################################
from urllib import request as re
from bs4 import BeautifulSoup as BS
import pandas as pd

###########################################

url = 'https://en.wikipedia.org/wiki/Queen_(band)' 
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')
name = bs.find('th',{'class':'infobox-above'}).text 
genre = bs.find('th',string = 'Genres').next_sibling.text
active = bs.find('span',string = 'Years active').parent.find_next_sibling('td').text

print(name)
print(genre)
print(active)

