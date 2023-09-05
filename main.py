from bs4 import BeautifulSoup
import requests


# connect to website
url = "https://www.amazon.in/DUDEME-Programmer-Coding-Developer-T-Shirt/dp/B08SFHKHV3/ref=sr_1_1?keywords=data+analyst+tshirt&qid=1693893082&sprefix=data+analyst+t%2Caps%2C310&sr=8-1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

http_proxy = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy = "ftp://10.10.1.10:3128"
proxyDict = {
              "http": http_proxy,
              "https" : https_proxy,
              "ftp": ftp_proxy
            }
page = requests.get(url, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

### TITLE ###
title = soup2.find("span", {"id":"productTitle"})
if title:
    title = title.get_text(strip=True)
else:
    title = "default_title"
print(title.strip())

### PRICE ###
price = soup2.find("span", {"class":"a-price-whole"})
if price:
    price = price.get_text(strip=True)
else:
    price = "default_title"
print(price.strip())

### DISCOUNT ###
dis = soup2.find("span", {"class":"a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage"})
if dis:
    dis = dis.get_text(strip=True)
else:
    dis = "default_title"
print(dis.strip())

### TYPE ###
typee = soup2.find("span", {"class":"a-list-item"})
if typee:
    typee = typee.get_text(strip=True)
else:
    typee = "default_title"
print(typee.strip())

### RATING ###
rat = soup2.find("span", {"class":"a-size-base a-color-base"})
if rat:
    rat = rat.get_text(strip=True)
else:
    rat = "default_title"
print(rat.strip())

# creating CSV
import csv
header = ["Product", "Price after discount", "Category", "Discount", "Rating"]
data = [title, price, dis, typee, rat]

# inserting data
with open("web scrapper dataset.csv", "w", newline="", encoding="utf8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

# appending data
with open("web scrapper dataset.csv", "a+", newline="", encoding="utf8") as f:  # appends the data at the next line which hasn't already been added to the dataset
    writer = csv.writer(f)
    writer.writerow(data)


