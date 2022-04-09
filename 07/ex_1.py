from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass
import datetime

####################IMPORTANT#####################
####################IMPORTANT#####################
######################----########################
######################----########################
######################----########################
######################----########################
###################-----------####################
####################---------#####################
######################-----#######################
#######################---########################
########################-#########################
###################################################
# Init for the tutor to run my programm: use your path and gekodriver 
##################################################################
# Init for the tutor to run my programm:
#gecko_path = '/opt/homebrew/bin/geckodriver'
#ser = Service(gecko_path)
#options = webdriver.firefox.options.Options()
#options.headless = False
#driver = webdriver.Firefox(options = options, service=ser)
##################################################################

# Init:
gecko_path = 'C:/Users/micha/Desktop/Selenium/chromedriver.exe'
ser = Service(gecko_path)
driver = webdriver.Chrome(service=ser) 


url = 'http://campuswire.com/signin'

# Actual program:
driver.get(url)

time.sleep(5)

username = driver.find_element(By.XPATH, '//input[@placeholder="Email"]')
my_email = input('Please provide your email:')
username.send_keys(my_email)

time.sleep(5)

password = driver.find_element(By.XPATH, '//input[@placeholder="password"]')
my_pass = getpass.getpass('Please provide your password:')
password.send_keys(my_pass)

time.sleep(5)

button = driver.find_element(By.XPATH, '//button[@type="submit"]')

button.click()

time.sleep(10)

chat = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/aside[1]/div/div[1]/ul/li[2]/button/i')
chat.click()

time.sleep(5)
person = driver.find_element(By.XPATH,"//*[contains(text(),'Maciej Wysocki')]")                                    
person.click()

time.sleep(5)

timestamp = datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")

driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/textarea').send_keys('Hello this is homework number 7 which sends itself!\n')
time.sleep(0.3)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/textarea').send_keys('It messaged at: ' + timestamp + '\n')
time.sleep(0.3)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/textarea').send_keys('Homework done by: ' + my_email + '\n')
time.sleep(0.3)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/button[1]/input').send_keys("C:/Users/micha/Desktop/instalacja/ex_1.py")
#### #IMPORTANT##################################################
#BELOW CHANGE THE PATH AND COMMENT LINE ABOVE 
#driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/button[1]/input').send_keys("PATH OF THIS PROGRAM ON YOUR COMPUTER")
time.sleep(10)


#Close browser:
driver.quit()

