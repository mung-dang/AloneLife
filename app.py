from flask import Flask, render_template
app = Flask(__name__)
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dblivealone

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)

driver.get('http://gs25.gsretail.com/gscvs/ko/products/event-goods')
wait = WebDriverWait(driver, 10)

gs_goods_name = []
gs_goods_img = []
gs_goods_price = []

i = 0
while i < 33:
    i += 1
    html_store = driver.page_source
    soup = BeautifulSoup(html_store, 'html.parser')
    goods = soup.find('ul', class_="prod_list")
    for good in goods:
        try:
            good_img = good.find('img')['src']
            gs_goods_img.append(good_img)
            good_name = good.find('p', class_="tit")
            gs_goods_name.append(good_name.text)
            good_price = good.find('p', class_="price")
            gs_goods_price.append(good_price.text)
        except:
            break

    driver.execute_script("goodsPageController.moveControl(1)")
    element2 = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="contents"]/div[2]/div[3]/div/div/div[1]/ul')))




@app.route('/')
def home():
   return render_template('index.html')

@app.route('/sign')
def life():
   return render_template('sign.html')

@app.route('/food')
def food():
   return render_template('food.html')

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
