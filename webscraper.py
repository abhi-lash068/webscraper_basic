import requests
from bs4 import BeautifulSoup

url = "https://www.webscraper.io/"

data = requests.get(url)

soup = BeautifulSoup(data.content, "html.parser")
print(soup.prettify())

# to print the title
print(soup.find_all('title'))

# to print body of the website
page_body = soup.body
print(page_body)

# to print head of the website
page_head = soup.head
print(page_head)

# using find() method
print(soup.find('link'))

# to print the paragraphs
paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    print(paragraph.text)
