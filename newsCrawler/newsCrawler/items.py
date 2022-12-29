import scrapy
from scrapy_djangoitem import DjangoItem
from base.models import News

class NewscrawlerItem(DjangoItem):
    django_model = News
