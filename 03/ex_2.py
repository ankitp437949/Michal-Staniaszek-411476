################################################################################
# Regex + Beautiful Soup.
################################################################################
# This script shows how to use powerful regex as another tool to navigate tags
from urllib import request
from bs4 import BeautifulSoup as BS
import re

url = 'https://en.wikipedia.org/wiki/United_Nations_Development_Programme'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

images = bs.find_all('img', {'src':re.compile('\/\/upload\.wikimedia\.org\/wikipedia\/[a-z]+\/[a-z]+\/[0-9a-z]+\/[0-9a-z]+\/Flag_of_[a-z_A-Z]+\.svg\/[0-9a-z-A-Z_]+\.svg\.png')})

for image in images:
    print(image['src'])

print('*****************Another way to include Belgium flag but less professional*************************************************')
images2 = bs.find_all('img', {'src':re.compile('.*Flag.*')})

for image in images2:
    print(image['src'])
