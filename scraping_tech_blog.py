import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

def scraping():
    url = 'https://techblog-matome.okdyy75.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    result = []
    yesterday = date.strftime(date.today() - timedelta(days=1), '%Y-%m-%d')
    for new_blog in soup.find_all(class_='partials__articleCard'):
      title = new_blog.find(class_='partials__articleCard__title').text.strip()
      company = new_blog.find(class_='partials__articleCard__blog').text.strip()
      description = new_blog.find(class_='partials__articleCard__description').text.strip()[:100] + '...'
      updated = new_blog.find(class_='partials__articleCard__created').text.strip()
      url = new_blog.find('a').get('href')
      if yesterday in updated:
        result.append([
            title, company, description, url
        ])
    return format_message(result)

def format_message(results):
  if len(results) == 0:
    return ["昨日投稿された技術ブログはないよ"] 

  messages = []
  for result in results:
    # messages.append('*['+result[0]+' （'+result[1]+'）]('+result[3]+')*'+'\n'+result[2])
    messages.append('*'+result[0]+'（'+result[1]+'）*\n'+result[3])
  return messages
