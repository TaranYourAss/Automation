from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import re
from datetime import date
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#collect data
file1 = open('t5008_data.txt', 'r')
Lines = file1.readlines()

#opens browser
driver = webdriver.Chrome('./chromedriver')
driver.get("http://turbotax.ca")
print("Please Login")
wait = input("Press Enter when you would like to continue")

#you must login to Turbo Tax and get to the T5008 page

#populates data
for line in Lines:
    regex = re.match("^(\d{2})\/(\d{2}) ([^ ]+) ([^ ]+) ([^\$]+)\$([^ ]+)[^\$]+\$([^ ]+)", line)
    parsed_date = "{}/{}/{}".format(regex.group(2), regex.group(1), date.today().year)
    box_14 = driver.find_element_by_xpath("//*[@id='Id9809']") #   Date of Disposition (dd/mm/yyyy)
    box_15 = driver.find_element_by_xpath("//*[@id='IdBox15']") #  Type code of securities
    box_16 = driver.find_element_by_xpath("//*[@id='Id9826']") #   Quantity of Securities 
    box_17 = driver.find_element_by_xpath("//*[@id='Id48305']") #  Identification of Securities 
    box_20 = driver.find_element_by_xpath("//*[@id='Id9800']") #   Cost or Book Value 
    box_21 = driver.find_element_by_xpath("//*[@id='IdBox21']") #  Proceeds or Settlement 
    
    #add WealthSimple data into the input boxes 
    box_14.send_keys(parsed_date)
    box_15.send_keys(regex.group(3))
    box_16.send_keys(regex.group(4))
    box_17.send_keys(regex.group(5))
    box_20.send_keys(regex.group(6))
    box_21.send_keys(regex.group(7))

    driver.find_element_by_xpath("//*[@id='blk_Bn9735']").click()
    time.sleep(2)
