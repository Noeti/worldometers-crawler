import scrapy
from ..utils import *
import json

class FossilfuelSpider(scrapy.Spider):
    name = 'fossil_fuel'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/energy']

    def __init__(self, category=None, *args, **kwargs):
        super(FossilfuelSpider, self).__init__(*args, **kwargs)
        self.fuel_type = f"{category}"
    
    def parse(self, response):
        countries = response.xpath('//tbody/tr')
        for country in countries:
            country_name = country.xpath('.//td/a/text()').get()
            url = response.urljoin(country.xpath('.//td/a/@href').get())
            yield scrapy.Request(
                url = url,
                callback=self.parse_fuel_link,
                meta={'name': country_name}
            )
    
    def parse_fuel_link(self, response):
        country_name = response.meta['name']
        path = f'//a[contains(@href,"{self.fuel_type}")]/@href'
        fuel_link = response.urljoin(response.xpath(path).get())

        yield scrapy.Request(
            url= fuel_link,
            callback=self.parse_country_fuel,
            meta= {'name': country_name},
        )
    
    def parse_country_fuel(self, response):
        country_name = response.meta['name']
        year = clean_year(response.xpath(f'//h3[contains(@id,"{self.fuel_type}")]/preceding::em/text()').get())
        units = response.xpath('//table//tr/td[position()=2]/text()').get()
        col_name = clean_names(clean_lst(response.xpath('//table[contains(@class,"table")]/tbody/tr/td/div[@align="left"]//text()').getall()))
        col_values = clean_values(clean_lst(response.xpath('//table[contains(@class,"table")]/tbody/tr/td[2]//text()').getall()))
        val_dict = {key:val for key,val in zip(col_name, col_values)}
        yield {
            'name': country_name,
            'values': val_dict,
            'year': year,
            'units': units
        }
  
