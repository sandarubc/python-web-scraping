import requests
import json

import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs,product_glomark):
    #TODO: Aquire the web pages which contain product Price
    la=requests.get(product_laughs)
    html1=BeautifulSoup(la.text,"html.parser")
    divs=html1("div")
    for div in divs:
        a=div.get("class")
        if a is not None and "product-name" in a:
            product_name_laughs=div.text
        if a is not None and "price-box" in a:
            price_laughs=div.text.split(".")
            price_laughs=int(price_laughs[1])+int(price_laughs[2])/100



    la2=requests.get(product_glomark,headers=user_agent)
    html2=BeautifulSoup(la2.text,"html.parser")
    scripts=html2("script")
    for script in scripts:
        if script.get("type")=="application/ld+json":
            js=json.loads(script.text)
            product_name_glomark=js["name"]
            price_glomark=float(js["offers"][0]["price"])
    
    
    #TODO: LaughsSuper supermarket website provides the price in a span text.


    #TODO: Glomark supermarket website provides the data in jason format in an inline script.
    #You can use the json module to extract only the price
    
    
    #TODO: Parse the values as floats, and print them.
    
    print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs)
    print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)
    
    if(price_laughs>price_glomark):
        print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
    elif(price_laughs<price_glomark):
        print('Laughs is cheaper Rs.:',price_glomark - price_laughs)    
    else:
        print('Price is the same')
if __name__=="__main__":
    product_laughs=r""+input("Enter Laugh URL: ")
    product_glomark=r""+input("Enter glomark URL: ")
    compare_prices(product_laughs,product_glomark)
