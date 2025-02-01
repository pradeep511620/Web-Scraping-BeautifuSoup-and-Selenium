import scrapy
from pkt_scraper.items import PktScraperItem  

class PlSpider(scrapy.Spider):
    name = "pl"
    allowed_domains = ["pkt.pl"]
    start_urls = ["https://www.pkt.pl/szukaj/firma/206"] #206

    def parse(self, response):
        # Extract and follow company links clicked to one by one  product page and get the data 
        for company in response.css(".company-name a::attr(href)").getall():
            if company:
                full_url = response.urljoin(company)
                self.logger.info(f"Company Link: {full_url}")
                yield response.follow(full_url, callback=self.parse_details, meta={"url": full_url})

        # Pagination: Find and follow the next page link
        next_page = response.css('li a[rel="next"]::attr(href)').get()
        if next_page:
            next_page_url = response.urljoin(next_page) 
            self.logger.info(f"Next Page: {next_page_url}")
            yield response.follow(next_page_url, callback=self.parse)

    def parse_details(self, response):
        item = PktScraperItem()

        item["url"] = response.meta["url"]
        item["name"] = response.css("h1.company-name::text").get(default='N/A').strip()
        item["category"] = response.css("div.company-category a::text").get(default='N/A').strip()
        
        address = ' '.join(response.css('div.box-company-street a span::text').getall()).strip()
        item["address"] = address if address else 'N/A'

        item["rating"] = response.css("div.company-rating .rating--number::text").get(default='N/A').strip()
        item["phone"] = response.css(".attr_shownumber::attr(data-phone)").get(default='N/A')
        item["website"] = response.css("span.www--full::text").get(default='N/A').strip()
        item["email"] = response.css('[data-popup="email-popup"] [data-tooltip="tooltip"]::attr(title)').get(default='N/A')
        item["social_links"] = response.css("div.box-social-link a::attr(href)").getall() or ['N/A']
        item["year_of_establishment"] = response.css('.cf.aggregated_item.aggregated-data__category.ptb10 .aggregated-content::text').get(default='N/A').strip()
        item["industry"] = response.css('.cf.full-company-data__item a::text').get(default='N/A').strip()

        self.logger.info(f"Item details: {item}")

        yield item
