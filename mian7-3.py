from urllib import response
import requests
from bs4 import BeautifulSoup
from sympy import continued_fraction_convergents

def get_exchange_rate(target1,target2):
    headers = {
        'User-Agent':'Mozilla/5.0',
        'Content-Type':'text/html;charset=utf-8'
    }
    response=requests.get("https://kr.investing.com/currencies/{}-{}".format(target1,target2),headers=headers)
    #print(response.content)
    content=BeautifulSoup(response.content,'html.parser')
    print(content)
    containers=content.find('span',{'id':'last_last'})
    print(containers)
    
get_exchange_rate('usd','krw')