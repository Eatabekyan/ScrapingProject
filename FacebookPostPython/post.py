import pyautogui
import os
import glob

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains

pyautogui.FAILSAFE = False

def start(driver):
	option = Options()
	option.add_argument("--disable-infobars")
	option.add_argument("start-maximized")
	option.add_argument("--disable-extensions")


	option.add_experimental_option("prefs", { 
	    "profile.default_content_setting_values.notifications": 2 
	})

	 
	driver.maximize_window()
	driver.get("https://www.facebook.com/")


def login(driver,id,password):
	email = driver.find_element_by_id("email")
	email.send_keys(id)
	Password = driver.find_element_by_id("pass")
	time.sleep(2)
	Password.send_keys(password)
	time.sleep(2)
	button = driver.find_element_by_name("login").click()
	pass
  
  

def create_post(driver,post):
	
	driver.get("https://www.facebook.com/greenautopartss")
	time.sleep(5)
	driver.execute_script("window.scrollTo(0, 4000)") 
	button = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]").click()
	time.sleep(10) 
	add_text(driver,post)
	time.sleep(10)
	add_photos(driver)
	time.sleep(30) 
	button = driver.find_element_by_xpath("//div[@aria-label='Опубликовать']").click()
	time.sleep(15) 
	pyautogui.click(1895,1055)
	time.sleep(15) 
	delete_photos()
	pass
  
  
def add_photos(driver):
	button = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]")
	button.click()
	pyautogui.press('left')
	time.sleep(2)
	pyautogui.press('down')
	time.sleep(2)
	pyautogui.press('down')
	time.sleep(2)
	pyautogui.press('enter')
	time.sleep(2)
	pyautogui.press('right')
	time.sleep(2)
	pyautogui.press('down')
	time.sleep(2)
	pyautogui.press('enter')
	time.sleep(2)
	pyautogui.hotkey('ctrl', 'a')
	time.sleep(10)
	pyautogui.press('enter')
	pass

def add_text(driver,text):
	actions = ActionChains(driver)
	for post in text:
		actions.send_keys(post)
		actions.send_keys(Keys.ENTER)
	actions.perform() 
	time.sleep(10)
	pass

def delete_photos():
	removingfiles = glob.glob('/home/eatabekyan/Downloads/facebook/*.jpg')
	for i in removingfiles:
		os.remove(i)

def posting(driver,content):
	create_post(driver,content)
  

