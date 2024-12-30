import scrapy

# create a class that inherits from scrapy.Spider
class BestBuySpider(scrapy.Spider):
    # spider and website identification
    name = 'bestbuy_spider'
    start_urls = [
        'https://www.bestbuy.com/site/searchpage.jsp?st=headphones'
    ]

    # method to parse the response using css selectors
    def parse(self, response):
        for product in response.css('li.sku-item'):
            yield {
                'Product Name': product.css('h4.sku-title a::text').get(),
                'Price': product.css('div.priceView-hero-price span[aria-hidden="true"]::text').get(),
                'True Price': product.css('div.pricing-price__regular-price span[aria-hidden="true"]::text').re_first(r'Was\s+\$(\d+\.\d+)'),
                'URL': response.urljoin(product.css('h4.sku-title a::attr(herf)').get())
            }