import requests
from bs4 import BeautifulSoup

def scraping():
    url = 'https://b.hatena.ne.jp/hotentry/it'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    result = []
    for top_news in soup.find_all(class_='entrylist-contents-main'):
      title = top_news.find(class_='entrylist-contents-title')
      users = top_news.find(class_='entrylist-contents-users')
      content = title.find('a')
      user_count = users.find('span')
      result.append([
          content.get('title'),
          content.get('href'),
          user_count.text
      ])
    return format_message(result[:5])

def format_message(results):
  messages = []
  for result in results:
    messages.append('*'+result[0]+' ('+result[2]+' users)*'+'\n'+result[1])
  return messages
