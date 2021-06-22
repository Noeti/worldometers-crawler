import scrapy
import json

from scrapy.http import request
from ..utils import *

class EnergySpider(scrapy.Spider):
    name = 'energy'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/energy/']

    def parse(self, response):
        #energy_columns = response.xpath('//table[@id="example2"]//span/text()').getall()
        countries = response.xpath('//tbody/tr')
        for country in countries:
            country_name = country.xpath('.//td/a/text()').get()
            energy_consumption_btu = clean_commas(country.xpath('.//td[3]/text()').get()) #BTU
            world_share = country.xpath('.//td[4]/text()').get()
            pc_yearly_btu = clean_commas(country.xpath('.//td[5]/text()').get()) #pc: per capita
            sources = response.xpath('//h3[contains(text(), "Sources")]/following::ul[1]/li/a/@href').getall()
            url = response.urljoin(country.xpath('.//td/a/@href').get())
            
            yield scrapy.Request(
                url = url,
                callback=self.parse_country_energy,
                meta={
                'name': country_name,
                'energy_consumption_btu': energy_consumption_btu,
                'world_share':world_share,
                'pc_yearly_btu': pc_yearly_btu,
                'sources': sources
            }
            )

    def parse_country_energy(self, response):
        country_name = response.meta['name']
        energy_consumption_btu =  response.meta['energy_consumption_btu']
        world_share = response.meta['world_share']
        pc_yearly_btu = response.meta['pc_yearly_btu'] 

        non_renewable = response.xpath('normalize-space((//div[contains(@style, "color:#999")])[1]/text())').get()
        oil_consump = clean_consump(response.xpath('//a[contains(text(), "Oil")]/following::text()').get())
        gas_consump = clean_consump(response.xpath('//a[contains(text(), "Gas")]/following::text()').get())
        coal_consump = clean_consump(response.xpath('//a[contains(text(), "Coal")]/following::text()').get())
        re_nuclear =  response.xpath('normalize-space((//div[contains(@style, "color:#999")])[2]/text())').get()

        yield {
            'name': country_name,
            'energy_consumption_btu': energy_consumption_btu,
            'world_share':world_share,
            'pc_yearly_btu': pc_yearly_btu,
            'non_renewable': non_renewable, 
            'oil_consump': oil_consump,
            'gas_consump': gas_consump,
            'coal_consump': coal_consump,
            're_nuclear': re_nuclear,
        }
        
        
            
    



        