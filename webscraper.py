from bs4 import BeautifulSoup
import requests
import re

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tag = doc.title
all_list_tags = doc.find_all("li")
tag.string = "Beautiful Soup Title Change"

# Testing with URL's 

url = "https://www.guitarcenter.com/Ibanez/TOD10N-Tim-Henson-Signature-Nylon-Acoustic-Electric-Guitar-Black-Flat-1500000386789.gc?icid=421588"
guitar_page = requests.get(url)

guitar_page_formatted = BeautifulSoup(guitar_page.text, "html.parser")

prices = guitar_page_formatted.find_all(text=re.compile(r'\$'))

# Additional searching functionality 

with open("index_two.html", "r") as f:
    doc_two = BeautifulSoup(f, "html.parser")

first_li_tag = doc_two.find("li")
first_li_tag["href"] = "#value has been changed#"
first_li_tag["style"] = "font-style: bold;"

all_p_tags = doc_two.find_all(["p"])
all_title_tags = doc_two.find_all(["h1", "h2", "h3"])

find_specific_li = doc_two.find_all(["li"], text="Contact Us")

# When searching for a class "class" is a reserved python key word so "class_" must be used

projects = doc_two.find_all(class_="project")

data_after_dollar_sign = doc_two.find_all(text=re.compile("\$.*"))

# limit number of results

first_three_lis = doc_two.find_all(["li"], limit=3)

# changing html document and saving 

tags = doc.find_all(["li"])

for tag in tags:
    tag = "THIS HAS BEEN CHANGED"

with open("changed.html", "w") as file:
    file.write(str(doc))

# navigating through html tree structure

coin_url = "https://coinmarketcap.com/"

coin_results = requests.get(coin_url).text

coin_doc = BeautifulSoup(coin_results, "html.parser")

tbody = coin_doc.tbody
table_rows = tbody.contents

prices = {}

for rows in table_rows[:10]:
    name, price = rows.contents[2:4]
    fixed_coin_names = name.p.string
    coin_prices = price.a.string

    prices[fixed_coin_names] = coin_prices

    print(prices)