import scrapy

# create a class that inherits from scrapy.Spider to define the spider that will crawl the website.
class AmazonSpider(scrapy.Spider):
    # name spider and website to crawl
    name = "amazon_spider"
    start_urls = [
        'https://www.amazon.com/s?k=laptop'
    ]

    # create a method to parse the response using css selectors
    def parse(self, response):
        for product in response.css('div.s-main-slot div.s-result-item'):
            yield {
                'Product Name': product.css('h2.a-size-medium.a-spacing-none.a-color-base.a-text-normal span::text').get(),
                'Price': product.css('span.a-offscreen::text').get(),
                'True Price': product.css('span.a-text-price span.a-offscreen::text').get(),
                'URL': product.css('a.a-link-normal.s-no-outline::attr(href)').get()
            }