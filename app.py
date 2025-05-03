from Scrappers.beautifulsoup import BeautyScrap
from Scrappers.selenium import SelenScrap

from ollama import chat
from ollama import ChatResponse

def ollama(prompt):
    response: ChatResponse = chat(model='llama3.2', messages=[
                            {
                                'role': 'user',
                                'content': prompt
                            },
                        ])

    print(response.message.content)

def getPrompt(title, content):
    return f"""You're an assistant. Summarize the content shortly with keypoints. 
            Title: {title}
            Content: {content}"""


scrapper = input("Enter 1 or 2: ")

if scrapper == "1":
    url = input("Enter the URL: ")    
    beautifulScrapper = BeautyScrap(url)
    
    ollama(
        getPrompt(beautifulScrapper.title, beautifulScrapper.text)
    )

elif scrapper == "2":
    query = input("Enter keywords to search website.")
    selenScrap = SelenScrap(query)
    
    ollama(
        getPrompt(selenScrap.title, selenScrap.text)
    )