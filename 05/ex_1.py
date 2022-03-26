################################################################################
# Scraping Single Wikipedia Page 
################################################################################
# This page exctracts links from single wikipedia page in a simplistic way:
from tkinter.ttk import Separator
from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

# Look at the page and the code
url = 'https://en.wikipedia.org/wiki/Lists_of_musicians' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find('span',id = 'A').parent.find_next_sibling('div').find_all('li')

links = ['http://en.wikipedia.org' + tag.a['href'] for tag in tags]

################################################################################
# This part prepares links
################################################################################
painter_links = []

for link in links:
    
    html = request.urlopen(link)
    bs = BS(html.read(), 'html.parser')
    
    tags = bs.find_all('ul')[1].find_all('li')

    link_temp_list = []
    for tag in tags:
        try:
            link_temp_list.append('http://en.wikipedia.org' + tag.a['href'])
        except:
            0 

    painter_links.extend(link_temp_list)


################################################################################
# This part scraps bands info  from the first link in  A_list 
################################################################################
d = pd.DataFrame({'name':[], 'Years of active':[]})


for painter_link in painter_links[0:39]:
   
    html = request.urlopen(painter_link)
    bs = BS(html.read(), 'html.parser')
    try:
        name = bs.find('h1').text
    except:
        name = ''
    try:
        active = bs.find('span',string = 'Years active').parent.find_next_sibling('td').get_text(separator =' ')

    except: 
        
        active = 0 
     
         

    band = {'name':name, 'Years of active' :active}     
    d = d.append(band, ignore_index = True)
    print(d)


#d.to_csv('Band_of_A.csv') #this part can save to CSV if you uncomment 



















