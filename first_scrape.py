# Here is some code on how to scare and save data to a CSV file.
# This is by no means advise to scrape any web site 

# Required files

import requests
from bs4 import BeautifulSoup
from csv import writer

# Code to scrape and save data into a file
response = requests.get('') #url goes here
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('article')

with open('blog_data.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(['title', 'link', 'date'])

    for article in articles:
        a_tag = article.find('a')
        title = a_tag.get_text()
        url = a_tag['href']
        date = article.find('time')['datetime']
        csv_writer.writerow([title, url, date])
