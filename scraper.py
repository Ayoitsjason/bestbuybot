import requests
from bs4 import BeautifulSoup
import smtplib, ssl
import time


# Get URL
URL = "https://www.theragun.com/us/en-us/pro-us.html"

# Get Header
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "jasonclebot@gmail.com"
password = "wsnvkrghlqbenfne"

context = ssl.create_default_context()

def check_price(): 
    page = requests.get(URL, headers=headers)

    print(page)

    # Storing parsed html page into a variable called soup
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("h1", {"class": "pdp-product-name"}).get_text()

    print(title.strip())

    price = soup.find("span", {"class": "product-price"}).get_text()
    converted_price = float(price[2:5])

    print(converted_price)

    if(converted_price < 550.0):
        print("Sending Email!")
        send_email()

def send_email():
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)

        subject = "Price fell down!"
        body = "https://www.theragun.com/us/en-us/pro-us.html"

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            'jasonclebot@gmail.com',
            'jasoncldev@gmail.com',
            msg
        )

        print("email has been sent!")

    except Exception as e:
        print(e)
    finally:
        server.quit()

while(True):
    check_price()
    time.sleep(5)