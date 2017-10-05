import scrapy

class QuotesSpider(scrapy.Spider):

    name = "quotes"


    # Scrapy는 Spider의 start_requests 메소드에 의해 리턴 된 요청 오브젝트를 스케줄링한다.
    # 각 요청에 대한 response인스턴스를 생성하며 요청에 할당된 콜백함수를 호출한다.
    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/'
        ]

        for url in urls:
            # url : 요청 url
            # callback : response시 호출될 콜백함수
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        self.log("******response*********" )
        self.log(response.url)
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename,'wb') as f:
            f.write(response.body)

        self.log('Saved file %s' % filename)
