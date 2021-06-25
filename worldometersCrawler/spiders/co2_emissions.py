import scrapy
from ..utils import clean_commas

class Co2EmissionsSpider(scrapy.Spider):
    name = 'co2_emissions'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/co2-emissions/co2-emissions-by-country']

    def parse(self, response):
        table = response.xpath('//table[@id="example2"]/tbody/tr')
        for row in table:
            country = row.xpath('.//td/a/text()').get()
            co2_emissions = clean_commas(row.xpath('.//td[3]/text()').get())
            one_year_change = row.xpath('.//td[4]/text()').get()
            population_2016 = clean_commas(row.xpath('.//td[5]/text()').get())
            per_capita = row.xpath('.//td[6]/text()').get()
            share_of_world = row.xpath('.//td[7]/text()').get()

            yield {
                'name': country,
                'co2_emissions_tons_2016': co2_emissions,
                'co2_emiss_one_year_change': one_year_change,
                'population_2016': population_2016,
                'co2_emiss_per_capita': per_capita,
                'country_share_of_world_co2': share_of_world
            }
