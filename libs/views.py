from django.views import View
from requests.exceptions import ConnectionError

from libs.response import json_response
from libs.res_code import Code, error_map


class SearchEngineSpiderView(View):
    """搜索引擎爬虫抽象视图"""
    spider_class = None

    def get(self, request):
        if not self.spider_class:
            raise ValueError("未指定爬虫类")
        key = request.GET.get("key")
        try:
            page_count = int(request.GET.get("page_count", 10))
        except ValueError as e:
            return json_response(result_code=Code.PARAM_ERR, message=f"{error_map[Code.PARAM_ERR]} {e}")

        try:
            spider = self.spider_class(key, page_count=page_count)
        except ConnectionError as e:
            return json_response(result_code=Code.CONNECT_ERR, message=f"{error_map[Code.CONNECT_ERR]} {e}")

        res = spider.run()

        data = res
        return json_response(data=data)
