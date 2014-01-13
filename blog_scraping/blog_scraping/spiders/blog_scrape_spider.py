from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from blog_scraping.items import BlogScrapingItem

class MySpider(BaseSpider):
	name = "upsouth"
	allowed_domains = ["blogspot.com"]
	start_urls = ["http://cowgirlimagery.blogspot.com/"]

	def parse(self, response):
		sel = Selector(response)
		posts = sel.xpath("//div[@class='post hentry']")
		items =[]
		for post in posts:
			item = BlogScrapingItem()
			item['title'] =post.xpath('//h3[@class="post-title entry-title"]').extract()
			item['content'] = post.xpath('//div[@class="post-body entry-content"]').extract()
			items.append(item)
		return items

