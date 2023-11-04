from bs4 import BeautifulSoup
import requests
import re

product = input("What product do you want to search for? ")

prices = {
    "New Egg": "",
    "Best Buy": "",
    "Amazon": ""
}

# New Egg

url = f"https://www.newegg.com/p/pl?d={product}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")


item_info_div = doc.find(["div"], class_="item-info") 

text = item_info_div.get_text() 
price = None

import re
price_match = re.search(r'\$(\d+\.\d{2})', text)

if price_match:
    price = price_match.group(0)
    prices["New Egg"] = price

