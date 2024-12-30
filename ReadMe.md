# Python Scraping

Scraping product data from Amazon and Best Buy, cleaning the data, and visualizing the average savings using pandas and seaborn.

## Setup

### Install Packages

```sh
pip install scrapy pandas seaborn matplotlib
```

## Run Tracker

- Navigate to project

```sh
cd winter_trend_tracker
```

- Run Amazon spider to scrape product data if json file missing:
```sh
scrapy crawl amazon_spider -o amazon_products.json
```

- Run Best Buy spider to scrape product data if json file missing:
```sh
scrapy crawl bestbuy_spider -o bestbuy_headphones.json
```

- Run 'pandas_scrap.py' script to clean the data, calculate savings, and visualize the average savings:
```sh
python pandas_scrap.py
```