from bs4 import BeautifulSoup
import requests
import re

product = input("What product do you want to search for? ")

url ="https://nuphy.com/collections/keyboards/products/{product}"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")



items = doc.find_all(text=re.compile(product))

print(items)

# for item in items:
#     print(item)
