# Scrapy settings for blog_scraping project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'blog_scraping'

SPIDER_MODULES = ['blog_scraping.spiders']
NEWSPIDER_MODULE = 'blog_scraping.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'blog_scraping (+http://www.yourdomain.com)'
