<<<<<<< HEAD
# Worldometers website crawler
The project contains three spiders:
* [population](https://www.worldometers.info/world-population/population-by-country/): scrapes population data by country and year.
* [energy](https://www.worldometers.info/energy/): scrapes energy consumption by country.
* fossil_fuel ([Oil](https://www.worldometers.info/oil/), [Natual Gas](https://www.worldometers.info/gas/), [Coal](https://www.worldometers.info/coal/)): scrapes energy data by fossil fuel type and country.

## Usage:

* **population.py sipder**:

  `scrapy crawl population -o population_dataset.json`
* **energy.py spider**: 

  `scrapy crawl energy -o energy_dataset.json`
* **Example for fuel_type = oil spider** (same for gas and coal):

  `scrapy crawl fossil_fuel  -a category=oil -o oil_dataset.json`

## Notes:
* **clean_dataset.ipynb**: 

  File used for data munging. Generates final .csv file ready to use. NaNs means no data available in this field.
||||||| merged common ancestors
=======
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
>>>>>>> df2c0a7da8701ce99b248960e922ff8ec87aacc0
