from parsingpart import extract_source
from parsingpart import extract_links
from parsingpart import extract_images
from parsingpart import extract_text
from parsingpart import download_images
from post import posting,start,login
import time
from work_info import append_list_as_row
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


last = 160
current = 1
driver = webdriver.Firefox()
start(driver)
time.sleep(1)
login(driver,"Login", "Password")
time.sleep(1)
for page in range(1,21):
	pg=21-page+1
	links = extract_links(extract_source(f'https://www.list.am/user/1080038?pg={pg}'))
	for link in links:
		if current >= last:
			print(link['href'])
			download_images(extract_images("https://www.list.am/"+link['href']))
			text = extract_text("https://www.list.am/"+link['href'])
			print(text)
			posting(driver,text)
			append_list_as_row('list.csv', [f'https://www.list.am/user/1080038?pg={pg}', 'https://www.list.am/'+link['href']])
			time.sleep(4)
		current+=1

