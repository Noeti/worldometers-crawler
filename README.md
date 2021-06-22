# Worldometers Scraper Project
This is a crawler to scrape [population](https://www.worldometers.info/world-population/population-by-country/) and [energy-related data](https://www.worldometers.info/energy/) from the website https://www.worldometers.info/ using scrapy. 

Feel free to use it, modify or suggest modifications.

## Requirements:
* Python 3.6+
* [Scrapy framework](https://github.com/scrapy/scrapy)

  ```
  pip install scrapy
  ```

## Usage:
1. `cd <project directory>`
2. For population or energy spiders: 

   `scrapy crawl <spider name> -o <output file name>.<json/csv>`
4. Fossil fuels (oil, natural gas, coal) spider:

   `scrapy crawl <spider name> -a category=<fossil fuel name> -o <output file name>.<json/csv>`
