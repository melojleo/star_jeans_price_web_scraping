from bs4 import BeautifulSoup
import requests 


url = 'https://www2.hm.com/en_gb/men/shop-by-product/jeans.html'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

products = soup.find('ul', class_='products-listing small')

product_list = products.find_all('article', class_='hm-product-item')

# Product id:
product_id = [p.get('data-articlecode') for p in product_list]

#produt category:
product_category = [p.get('data-category') for p in product_list]

#produt name:
#product_name = [p.get('data-category') for p in product_list]
product_list = products.find_all('a', class_='link')
product_name = [p.get_text() for p in product_list]
print(product_category)
