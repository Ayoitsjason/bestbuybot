import requests
from bs4 import BeautifulSoup

URL = "https://www.theragun.com/us/en-us/pro-us.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}

page = requests.get(URL, headers=headers)

print(page)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup)

