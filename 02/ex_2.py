#############################################
from urllib import request as re
from bs4 import BeautifulSoup as BS
import pandas as pd

###########################################

url = 'https://en.wikipedia.org/wiki/Pawe%C5%82_Domaga%C5%82a' 
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')
###########################################
# #BIRTHDAY
bday = bs.find('span', {'class':'bday'}).text

# #OCCUPATION
occ_list = bs.find_all('div',{'class':'hlist hlist-separated'})

#REFERENCES 
bs_ref_list = bs.find_all('ol',{'class':'references'})

#####PRINT
print(bday)

for name in occ_list:
    print(name.get_text(separator=" "))

for name in bs_ref_list:
    print(name.get_text())