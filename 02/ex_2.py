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
occ = bs.find('td', {'class':'infobox-data role'}).text
occ1 = occ[0:5]
occ2 = occ[5:11]
occ3 = occ[11:21]

#REFERENCES 
bs_ref_list = bs.find_all('ol',{'class':'references'})

#####PRINT
print(bday)
print("%s %s %s" %(occ1,occ2,occ3))

for name in bs_ref_list:
    print(name.get_text())