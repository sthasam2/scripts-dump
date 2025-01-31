import csv

import requests
from bs4 import BeautifulSoup as bs

a = requests.get("https://kalimatimarket.gov.np/")
soup = bs(a.text, "lxml")
table = soup.find("table")
data = [doc.get_text().split("रू ") for doc in table.find_all("tr")][1:]

with open("price_list.csv", "w") as output_file:
    writer = csv.writer(output_file, delimiter=",")
    writer.writerows(data)
