from bs4 import BeautifulSoup 
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium import webdriver
from lxml import etree
import time

driver = webdriver.Chrome()

try:
    driver.get('https://www.instagram.com/')
    time.sleep(5)
    login_input = driver.find_element(By.NAME,"username").send_keys("rezanans_nikita")
    time.sleep(3)
    password_input = driver.find_element(By.NAME,"password").send_keys("N02081996rezanans!!"+Keys.ENTER)
    time.sleep(10)
    driver.get('https://www.instagram.com/margo.novik/')
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, "lxml")
    print(int(soup.find('ul').find_all('li')[0].find_all('span')[0].text.replace(u'\xa0',u'')))
    print(int(soup.find('ul').find_all('li')[1].find_all('span')[0]['title'].replace(u'\xa0',u'')))
    print(int(soup.find('ul').find_all('li')[2].find_all('span')[0].text.replace(u'\xa0',u'')))
    # print(soup.find_all('section')[0].find('section').find_all('div'))
    xpath = etree.HTML(str(soup))
    print(xpath.xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/span')[0].text)
    print(xpath.xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/h1')[0].text)
    # print(soup.find_all('section')[0].find('section').find_all('div')[2].find('h1').text)
except Exception as ex:
    print(ex)
finally:
    driver.quit()
