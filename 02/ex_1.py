#############################################
from urllib import request as re
from bs4 import BeautifulSoup as BS
import pandas as pd

###########################################
url = 'http://www.pythonscraping.com/pages/page3.html' 
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')
#####BOLD####### 
bs_name_list = bs.find_all('span', {'class':'excitingNote'})
for name in bs_name_list:
    print(name.get_text())
#LIST
name_list = [name.get_text() for name in bs_name_list]
#PRINT
d = pd.DataFrame(name_list)
print(d)

#####ITEM TITLE####### 
item = bs.find('tr', {'id':'gift5'}).td.text

print(item)

#FOOTER
ft = bs.find('div', {'id':'footer'}).text
print(ft)




