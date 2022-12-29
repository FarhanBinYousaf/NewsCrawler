from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from base.models import News

class DuplicatesPipeline:

    def __init__(self):
        self.links_seen = set()
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['link'] in self.links_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.links_seen.add(adapter['link'])
            return item

class NewscrawlerPipeline(object):

    def process_item(self, item, spider):
        item.save()
        return item
