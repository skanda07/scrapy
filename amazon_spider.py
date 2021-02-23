import scrapy
from ..items import AmazonedaItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    #allowed_domains = ['amazon.com']
    pagenumber=2
    start_urls = [
        'https://www.amazon.in/s?i=electronics&bbn=1389401031&rh=n%3A1389401031%2Cp_89%3ARedmi%7CSamsung&dc&qid=1611370413&rnid=3837712031&ref=sr_nr_p_89_3'
                  ]

    def parse(self, response):
        items=AmazonedaItem()
        model_name=response.css('.a-color-base.a-text-normal::text').extract()
        model_price=response.css('.a-price-whole::text').extract()
        model_ratings=response.css('span.a-icon-alt::text').extract()
        delivery_type=response.css(".sg-col-12-of-16:nth-child(6) .a-icon-medium , .AdHolder+ .sg-col-12-of-16 .s-align-children-center span , .s-align-children-center .s-align-children-center+ .a-row span").css("::text").extract()                                                 
        delivery_type = [x.strip() for x in delivery_type]
        model_ratings = [x.split(' ')[0] for x in model_ratings]

        for models in zip(model_name,model_price,model_ratings,delivery_type):
            items['model_name']=models[0] 
            items['model_price']=models[1]          
            items['model_ratings']=models[2]
            items['delivery_type']=models[3]
            yield items
       
        nextpage='https://www.amazon.in/s?i=electronics&bbn=1389401031&rh=n%3A1389401031%2Cp_89%3ARedmi%7CSamsung&dc&page='+ str(AmazonSpiderSpider.pagenumber)+'/'
       
        if AmazonSpiderSpider.pagenumber <= 37:
            AmazonSpiderSpider.pagenumber+=1
            yield response.follow(nextpage, callback=self.parse)

        # pass
