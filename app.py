from Scrappers.beautifulsoup import BeautyScrap
from Scrappers.selenium import SelenScrap

# selenScrap = SelenScrap("muslim world league")

def output(title, text):
    print(title)
    print(text)

scrapper = input("Enter 1 For Beautiful Soup and 2 For Selenium.")

if scrapper == 1:
    url = input("Enter the URL: ")
    
    beautifulScrapper = BeautyScrap(url)
    output(beautifulScrapper.title, beautifulScrapper.text)

elif scrapper == 2:
    query = input("Enter keywords to search website.")
    selenScrap = SelenScrap(query)
    output(selenScrap.title, selenScrap.text)