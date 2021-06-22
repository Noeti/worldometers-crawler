import scrapy

class PopulationSpider(scrapy.Spider):
    name = 'population'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            url = country.xpath(".//@href").get()

            # absolute_url = f'https://www.worldometers.info{url}'
            absolute_url = response.urljoin(url)

            yield scrapy.Request(
                url=absolute_url,
                callback=self.parse_country,
                meta={
                    'country_name': name
                }
            )
    def parse_country(self, response):
        table = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        name = response.meta["country_name"]
        for row in table:
            year = row.xpath('.//td[1]/text()').get()
            population = row.xpath('.//td/strong/text()').get()
            yield {
                'country_name': name,
                'year': year,
                'count': population
            }
