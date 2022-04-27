from django.views import View

from libs.views import SearchEngineSpiderView, SimpleViewSet
from libs.response import json_response
from apps.spider.models import BtAndVulBoxModel
from spider.spiders import BaiduSearchSpider, GoogleSearchSpider, TdFingerSearchSpider

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


class TideFingerSearchSpiderView(View):
    """潮汐指纹在线爬虫"""

    def get(self, request):
        domain = request.GET.get("domain")
        spider = TdFingerSearchSpider(domain)
        res = spider.get_finger_data()
        if not res:
            return json_response("TideFinger Cookie 失效，请重新设置")
        return json_response(data=res)
