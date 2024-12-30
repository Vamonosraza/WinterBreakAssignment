import scrapy

class BestBuySpider(scrapy.Spider):
    name = 'bestbuy_spider'
    start_urls = [
        'https://www.bestbuy.com/site/searchpage.jsp?st=headphones'
    ]

    def parse(self, response):
        for product in response.css('li.sku-item'):
            yield {
                'Product Name': product.css('h4.sku-title a::text').get(),
                'Price': product.css('div.priceView-hero-price span[aria-hidden="true"]::text').get(),
                'True Price': product.css('div.pricing-price__regular-price span[aria-hidden="true"]::text').re_first(r'Was\s+\$(\d+\.\d+)'),
                'URL': response.urljoin(product.css('h4.sku-title a::attr(herf)').get())
            }