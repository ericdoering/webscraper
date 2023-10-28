from bs4 import BeautifulSoup
import requests
import re

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tag = doc.title
all_list_tags = doc.find_all("li")
tag.string = "Beautiful Soup Title Change"

# Testing With URL's 

url = "https://www.guitarcenter.com/Ibanez/TOD10N-Tim-Henson-Signature-Nylon-Acoustic-Electric-Guitar-Black-Flat-1500000386789.gc?icid=421588"
guitar_page = requests.get(url)

guitar_page_formatted = BeautifulSoup(guitar_page.text, "html.parser")

prices = guitar_page_formatted.find_all(text=re.compile(r'\$'))

print(prices)