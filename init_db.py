import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)

driver.get('https://cu.bgfretail.com/event/plus.do?category=event&depth2=1&sf=N')

cu_goods_name = []
cu_goods_img = []
cu_goods_price = []

driver.execute_script("javascript:goDepth('23');")
i = 0
while i < 4:
    driver.execute_script("javascript:nextPage(1);")
    i += 1

while len(cu_goods_name) % 40 == 0:
    html_store = driver.page_source
    soup = BeautifulSoup(html_store, 'html.parser')
    goods = soup.find_all('li', class_="prod_list")
    for good in goods:
        good_img = good.find('img')['src']
        if good_img in 'https:':
            cu_goods_img.append(good_img)
        else:
            cu_goods_img.append('https:' + good_img)
        good_name = good.find('div', class_="name")
        cu_goods_name.append(good_name.text)
        good_price = good.find('div', class_="price")
        cu_goods_price.append(good_price.text)

print(cu_goods_name)
print(cu_goods_img)
print(cu_goods_price)