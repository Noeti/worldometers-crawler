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
