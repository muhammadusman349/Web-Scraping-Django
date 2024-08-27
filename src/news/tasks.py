import logging
import requests
from celery import shared_task
from .models import News
from bs4 import BeautifulSoup
from datetime import datetime


logger = logging.getLogger(__name__)


@shared_task
def log_message():
    logger.info("Task is running every 30 seconds")
    return "Task is running"

@shared_task
def add(x, y):
    return x + y

@shared_task(serializer='json')
def send_article_to_db(articles_list):
    count = 0
    for article in articles_list:
        try:
            News.objects.create(
                title=article['title'],
                link=article['link'],
                published=article['published'],
                )
            count +=1
        except Exception as e:
            print(e)
            print("task failed an error occured")


@shared_task(name="scrape_hacker_new_rss_feed")
def scrape_hacker_new_rss_feed():
    articles_list = []
    try:
        res = requests.get("https://news.ycombinator.com/rss")
        soup = BeautifulSoup(res.content, features='xml')
        articles = soup.findAll('item')
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            published_date = a.find('pubDate').text
            published = datetime.strptime(published_date, '%a, %d %b %Y %H:%M:%S %z')

            article={
                'title': title,
                'link': link,
                'published': published,
            }
            articles_list.append(article)
        return send_article_to_db.delay(articles_list)
    except Exception as e:
        print(e)
        print('task failed an error occured')
