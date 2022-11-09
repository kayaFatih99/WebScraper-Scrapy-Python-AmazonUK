import scrapy
from scrapy.utils.response import open_in_browser
from ..items import AmazonItem

class AmazonSearchSpider(scrapy.Spider):
    name = 'amazon_search'
    allowed_domains = ['www.amazon.co.uk']

    def start_requests(self):
        print("""
            Desihned for Amazon UK
            Amazon product search and data extraction application
            
            Steps to follow :
                1   -   Indicate in which category you want to search. (Press enter to search all categories.) (Str)
                2   -   You must enter search text. (Str)
                3   -   Now you can start shooting data.

            Important :
                Tested only on amazon UK and in all categories within categories. This code may also give errors to 
            different amazon pages. It can be updated according to the desired features.
        """)  

        search = []
        category = int(input(f"page data : Please specify product category. (Exp: (Enter :) ) => All category) => "))
        text = input(f"page data : Please enter search text. (Exp : baby car) => ")
        search.append(f'https://www.amazon.co.uk/s?k={text}&i={category}')

        start_urls = search
        for url in start_urls:
            print(f'url bilgisi => {url}')
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = AmazonItem()

        products = response.xpath("//div[@data-component-type='s-search-result']")
        for product in products:
            productNumber = product.xpath(".//div/div/@data-csa-c-pos").get()
            productAsin = product.xpath(".//@data-asin").get()
            productUuid = product.xpath(".//@data-uuid").get()
            productImageLink = product.css(".s-latency-cf-section.s-card-border .s-image-square-aspect .s-image").css('::attr(src)').get()
            productLink = product.css(".s-latency-cf-section.s-card-border .s-height-equalized > span > a").css("::attr(href)").get()     
            productTitle = product.css(".s-latency-cf-section.s-card-border h2.a-size-mini").css("::text").get()
            productStar = product.css(".s-latency-cf-section.s-card-border .aok-align-bottom > span").css("::text").get()
            numberComment = product.css(".s-latency-cf-section.s-card-border .s-link-style .s-underline-text").css("::text").get()
            productPriceOne = product.css(".s-latency-cf-section.s-card-border .a-price-whole").css("::text").get()
            productPriceTwo = product.css(".s-latency-cf-section.s-card-border .a-price-fraction").css("::text").get()
            productOldPrice = product.css(".s-latency-cf-section.s-card-border .a-text-price .a-offscreen").css("::text").get()

            sterlinIcon = '£'
            productPrice = None
            if productPriceOne and productPriceTwo is None:
                productPrice = None
            elif productPriceOne and productPriceTwo is not None:
                productPrice = f'{sterlinIcon}{productPriceOne}.{productPriceTwo}'
           
            discountRateTwo = None
            if productOldPrice is None:
                pass
            elif productOldPrice is not None:
                discountPrice = productOldPrice.lstrip("£")
                orginalPrice = productPrice.lstrip("£")
                discountRateOne = (1 - float(orginalPrice) / float(discountPrice)) * 100
                discountRateTwo = str(round(discountRateOne, 2))
                discountRateTwo = f'%{discountRateTwo}'

            items['productNumber'] = productNumber
            items['productAsin'] = productAsin
            items['productUuid'] = productUuid
            items['productImageLink'] = productImageLink
            items['productLink'] = f'https://www.amazon.co.uk/{productLink}'
            items['productTitle'] = productTitle
            items['productStar'] = productStar
            items['numberComment'] = numberComment
            items['productPrice'] = productPrice
            items['productOldPrice'] = productOldPrice
            items['discountRate'] = discountRateTwo

            yield items 
                   
        
        next_page = response.xpath("//div[@role='navigation' and @class='a-section a-text-center s-pagination-container']/span[@class='s-pagination-strip']/a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']/@href").get()
            
        if next_page:
            full_link = f'https://www.amazon.co.uk/{next_page}'
            print(f"sonraki sayfa link => {full_link}")
            yield scrapy.Request(url=full_link, callback=self.parse)
        
        open_in_browser(response)
        

