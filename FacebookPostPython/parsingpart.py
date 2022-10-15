from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import os
import pyautogui
import time


def extract_source(url):
     agent = {"User-Agent":"Mozilla/5.0"}
     source=requests.get(url, headers=agent).text
     return source

def extract_links(source):
	soup=BeautifulSoup(source, 'lxml')
	names=soup.find('div',{"class":"gl"})
	links = names.findAll('a')
	return links

def extract_images(url):
	if url is None:
		return None
	images=list()
	Driver = webdriver.Firefox()
	Driver.get(url)
	for j in range(20):
		l=Driver.find_elements_by_class_name("right")
		if len(l)==0:
			break
		else:
			l1 = Driver.find_element_by_class_name("right")
			l1.click()
		time.sleep(2)
	p = Driver.find_element_by_xpath("""//div[@class='p']""")
	elements= p.find_elements_by_tag_name("img")
	for i in  elements:
    		img_src = i.get_attribute("src")
    		images.append(img_src)
    	
	Driver.quit()
	return images

def extract_text(url):
	text=list()
	source=extract_source(url)
	soup=BeautifulSoup(source, 'lxml')
	vih=soup.find('div',{'class':'vih'})
	span=vih.find('span')
	if span is not None:
		price=span['content']+'֏'

	body=soup.find('div',{'class':'body', "itemprop": "description"})
	txt1=body.findAll(text=True)
	text.append('🟩')
	for i in txt1:
		if i == txt1[1] and span is not None:
			text.append("Գինը՝ "+price)
		text.append(i)
	text.append('Հեռ․ 044 322222')
	return text
		
def download_images(images):
	if images is None:
		pass
	i = 1
	driver = webdriver.Firefox()
	for imgURL in images:
		driver.get(imgURL)
		pyautogui.hotkey('ctrl', 's')
		time.sleep(5)
		pyautogui.hotkey('ctrl', 'a')
		time.sleep(4)
		pyautogui.press('delete')
		time.sleep(4)
		pyautogui.write(f'/home/eatabekyan/Downloads/facebook/{i}.jpg')
		time.sleep(5)
		pyautogui.press('enter')
		i+=1
		time.sleep(2)
	driver.quit()
		


	
