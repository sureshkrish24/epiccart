import requests
import bs4
from fake_headers import Headers
import json

def ajioSearch(x):
    url = "https://www.ajio.com/search/?text={0}"
    url = url.format(x)
    page = requests.get(url, headers=Headers(os='win',browser='chrome',headers=True).generate())
    # html = page.content
    page_soup = bs4.BeautifulSoup(page.content, "html.parser")
    # print(page_soup)
    # ajio=page_soup.findAll('div',attrs={'role':'row'})
    d=json.loads(str(page.content))
    print(d)
    ajio=page_soup.find('div',class_='brand')
    print(page_soup)
    # for div in ajio:
    #     d={}
    #     b=div.find('div',class_='brand')
    #     p=div.find('span',class_='price')
    #     n=div.find('div',class_='nameCls')
    #     i=div.find('img',class_='rilrtl-lazy-img rilrtl-lazy-img-loaded')
    #     l=div.find('a')
    #     r='Nill'
    #     if(b!=None and p!=None and n!=None and i!=None and l!=None):
    #         d["Name"]=n.text
    #         d["Price"]=p.text
    #         d["Brand"]=p.text
    #         d["ProductLink"]="https://www.ajio.com"+l.get('href')
    #         d["Image"]=i.get('src')
    #         d["Rating"]=r
    #         d["FA"]="Ajio"
    #         d["ID"]="Nill"
    #         # Data.append(d)
            # print(d)
ajioSearch('Shoe')
