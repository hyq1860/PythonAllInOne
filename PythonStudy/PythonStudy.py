from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.cnblogs.com/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        print response.doc('title').text()
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }

    def on_result(self, result):
        #your_db.save(result)
        super(Handler, self).on_result(result)