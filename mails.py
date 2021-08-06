import os
import requests
import re
import time
from bs4 import BeautifulSoup as bs
import smtplib, ssl


def send_mail(product_name,price,id):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "palakshivlani2001@gmail.com"  # Enter your address
    #receiver_email = "shivlanipalak@gmail.com"  
    receiver_email = id 
    password = "palak2001"
    message = """Subject: Price Notification

    Hi {product}, is at price {price}.Book Now!"""
    
    

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.format(product=product_name,price=price).encode('ascii', 'ignore').decode('ascii'))


def check_fk_price(url, amount, id):

    request = requests.get(url)
    soup = bs(request.content,'html.parser')

    product_name = soup.find("span",{"class":"B_NuCI"}).get_text()
    price = soup.find("div",{"class":"_30jeq3 _16Jk6d"}).get_text()
    prince_int = int(''.join(re.findall(r'\d+', price)))
    print(product_name + " is at " + price)
    text = product_name + "is at " + price
    if prince_int < amount:
        print("Book Quickly")
        send_mail(product_name,price,id)
    else:
        print("No Slots found")


def main():
#    send_mail()
#    URL = "https://www.flipkart.com/apple-watch-series-6-gps-40-mm-space-grey-aluminium-case-black-sport-band/p/itm43bb5a1d8bf7c?pid=SMWFVNKG9H3EEZFZ&lid=LSTSMWFVNKG9H3EEZFZEUMSTT&marketplace=FLIPKART&q=apple+watch+series+6&store=ajy%2Fbuh&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_5_4_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_5_4_na_na_na&fm=SEARCH&iid=f45a1c36-9d51-46ad-b04e-209815042dcb.SMWFVNKG9H3EEZFZ.SEARCH&ppt=browse&ppn=browse&ssid=2av24d7x218z1ts01628166951810&qH=b4ac3f371ff9d2af"
    URL = input("Input the url of the product : " )
    wantprice = input("Input the price of the product on which you want to buy :")
    id = input("Please enter your mail id : ")
    while True:
        check_fk_price(URL, int(wantprice), id)
        time.sleep(3600)



if __name__ == "__main__":
    main()