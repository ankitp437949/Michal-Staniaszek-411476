################################################################################
# Lambda expressions + Beautiful Soup.
################################################################################
# This script uses lambda expressions with find_all func. to search for tags:
from urllib import request
from bs4 import BeautifulSoup as BS

url = 'http://www.pythonscraping.com/pages/warandpeace.html' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')
############################ Part 1 ##########################################
selected_tags = bs.find_all(lambda tag: ('Anna Pavlovna' in tag.get_text()))
print(len(selected_tags))
############################ Part 2 ##########################################
one_attribute_tags = bs.find_all(lambda tag: (len(tag.attrs) == 1))
for tag in one_attribute_tags:
    print('*****************')
    print(tag.get_text())

print(len(one_attribute_tags))
