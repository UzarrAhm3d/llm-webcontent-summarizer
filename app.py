import sys
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Muslim_World_League"

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.string

    print(f"Page Title: {title}")
    
    introductions  = soup.find_all('p')
    
    for intro in introductions[:5]:
        print(f"Introduction: {intro.text}")
        



# sys.exit()

print("Hello World")