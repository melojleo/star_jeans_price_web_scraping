from bs4 import BeautifulSoup
import requests 


url = 'https://www2.hm.com/en_gb/men/shop-by-product/jeans.html'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

products = soup.find('ul', class_='products-listing small')

product_list = products.find_all('article', class_='hm-product-item')
print(product_list[0])
