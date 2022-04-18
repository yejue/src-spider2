from libs.views import SearchEngineSpiderView
from spider.spiders import BaiduSearchSpider, GoogleSearchSpider

# Create your views here.


class BaiduSearchSpiderView(SearchEngineSpiderView):
    """百度搜索爬虫视图"""
    spider_class = BaiduSearchSpider


class GoogleSearchSpiderView(SearchEngineSpiderView):
    """谷歌搜索爬虫视图"""
    spider_class = GoogleSearchSpider
