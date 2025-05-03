import sys
import requests
from bs4 import BeautifulSoup

class BeautyScrap:

    url: str
    title: str
    text: str

    def __init__(self, url):
        
        response = requests.get(url)

        if response.status_code == 200:
            
            soup = BeautifulSoup(response.text, 'html.parser')

            self.title = soup.title.string

            print(f"Page Title: {self.title}")
            
            for irrelevant in soup.body(["script", "style", "img", "input", "header", "nav"]):
                irrelevant.decompose()
            
            # print(soup.body)
            # header = soup.body.find("header")
            # if header:
            #     header.decompose()
            
            self.text = soup.body.get_text(separator="\n", strip=True)