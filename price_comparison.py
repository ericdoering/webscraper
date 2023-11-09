from bs4 import BeautifulSoup
import requests
import re
import xml.etree.ElementTree as ET
import webbrowser

product = input("What product do you want to search for? ")

prices = {
    "New Egg": "",
    "Item Emporium": "",
    "Game Zone Products": ""
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

# Item Emporium (Fake E-Commerce Site)

with open("item_emporium.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
    

product_name_tag = doc.find("h2", text="NVIDIA GeForce RTX 3080 Graphics Card")

if product_name_tag:

    price_tag = product_name_tag.find_next("p", class_="price")

    if price_tag:
        price = price_tag.text
        prices["Item Emporium"] = price
else:
    print("Product name tag not found in the HTML.")


# Game Zone Products (Fake E-Commerce Site)

with open("game_zone_products.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")


    product_name_tag = doc.find("h1", text="NVIDIA GeForce RTX 3080 Graphics Card")

    if product_name_tag:

        price_tag = product_name_tag.find_next("div", class_="price")

        if price_tag:
            price = price_tag.text
            prices["Game Zone Products"] = price

final_prices = {key: value.replace('\n', '') for key, value in prices.items()}


html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Prices</title>
</head>
<body>
    <ul>
"""

for store, price in final_prices.items():
    html_content += f"        <li>{store}: {price}</li>\n"
html_content += """
    </ul>
</body>
</html>
"""

with open("prices.html", "w") as html_file:
    html_file.write(html_content)