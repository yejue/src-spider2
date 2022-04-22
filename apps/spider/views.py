from libs.views import SearchEngineSpiderView, SimpleViewSet
from apps.spider.models import BtAndVulBoxModel
from spider.spiders import BaiduSearchSpider, GoogleSearchSpider

# Create your views here.


class BaiduSearchSpiderView(SearchEngineSpiderView):
    """百度搜索爬虫视图"""
    spider_class = BaiduSearchSpider


class GoogleSearchSpiderView(SearchEngineSpiderView):
    """谷歌搜索爬虫视图"""
    spider_class = GoogleSearchSpider


class BtAndVulBoxDataViewSet(SimpleViewSet):
    """补天&漏洞盒子爬虫任务数据展示视图"""
    operation_fields = ["id", "company_name", "test_range", "property_range", "origin", "origin_url"]
    model = BtAndVulBoxModel
    base_name = "bt-vulbox"
