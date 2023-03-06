from bs4 import BeautifulSoup
import requests 
import pandas as pd
import numpy as np
from datetime import datetime



url = 'https://www2.hm.com/en_gb/men/shop-by-product/jeans.html'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

#Total item and pages
total_item = soup.find_all('h2', class_='load-more-heading')[0].get('data-total')
total_item = int(total_item)
page_number = np.round(int(total_item)/36)

#Final Url
url02 = url + '?page-size=' + str(int(page_number*36))
page = requests.get(url02, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

#list of all products
products = soup.find('ul', class_='products-listing small')

# Product id:
product_list = products.find_all('article', class_='hm-product-item')
product_id = [p.get('data-articlecode') for p in product_list]

#produt category:
product_category = [p.get('data-category') for p in product_list]

#produt name:
product_list = products.find_all('a', class_='link')
product_name = [p.get_text() for p in product_list]

#price:
product_list = products.find_all('span', class_='price regular')
product_price = [p.get_text() for p in product_list]

#color

#composition

data_raw = pd.DataFrame([product_id, product_category, product_name, product_price]).T
data_raw.columns = ['product_id', 'product_category', 'product_name', 'product_price']
 
#srapy datetime
data_raw['scrapy_datetime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
 
print(data_raw)
