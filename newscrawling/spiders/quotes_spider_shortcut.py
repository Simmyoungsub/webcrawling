import scrapy

class QuotesSpider(scrapy.Spider):

    name = "quotes_shortcut"

    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        # 'https://quotes.toscrape.com/page/2/'
    ]

    def parse(self,response):
        # self.log("******response*********" )
        # self.log(response.url)
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename,'wb') as f:
        #     f.write(response.body)
        #
        # self.log('Saved file %s' % filename)
        for quote in response.css('div.quote'):
            yield{
                'text' : quote.css('span.text::text').extract_first(),
                'author' : quote.css('span.small::text').extract_first(),
                'tags' : quote.css('div.tags a.tag::text').extract()
            }

        next_page = response.css('li.next a::attr(href)').extract_first()

        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
