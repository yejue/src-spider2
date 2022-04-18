import requests
import time
import random
import brotli  # 隐式依赖

from bs4 import BeautifulSoup
from . import constants


class BaiduSearchSpider:
    """百度搜索爬虫

        1. 条目筛选：只取实际词条，百度百科、百度贴吧、广告与聚合视频不取
        2. 页数筛选：默认取 10 页
        3. 返回类型：json/dict
    """

    url_model = constants.BAIDU_URL_MODEL
    headers = constants.BAIDU_HEADERS

    def __init__(self, key, page_count=10, is_log=True):
        self.key = key
        self.page_count = page_count
        self.is_log = is_log  # 爬行记录

        self.session = requests.Session()
        self.session.get("https://www.baidu.com/")  # 初次访问模拟

    def get_page(self, key, n, buffer_num=0):
        """取第 n 页"""
        res = []

        if buffer_num > 5:  # 最多缓冲 5 次则不再请求
            return res

        url = self.url_model.format(key, (n-1)*10)
        req = self.session.get(url, headers=self.headers)
        data = req.content.decode("utf8")  # 页面资源

        if data == "\n":
            print(f"[Warning] - {req.headers}")

        soup = BeautifulSoup(data, "html.parser")  # BS 筛选对象
        soup_temp = soup.select(".result.c-container")  # 筛选除广告与百度百科等以外的条目

        for item in soup_temp:
            try:
                title = item.select_one(".c-title a").text
            except:
                time.sleep(random.randint(1, 10)/10)  # 缓冲时间
                print("[REBOOT]缓冲重启中 ...")
                buffer_num += 1
                return self.get_page(key, n, buffer_num)
            res.append({"title": title, "url": item.attrs["mu"]})
        return res

    def get_pages(self, key, page_count):
        """取 n 页"""
        res = []

        for i in range(1, page_count + 1):
            temp = self.get_page(key, i)

            if self.is_log:
                print(f"[{i}] - 获取数量：{len(temp)}")

            res.extend(temp)
            time.sleep(random.randint(1, 10) / 10)  # 缓冲时间
        return res

    def run(self):
        """自主爬行任务"""
        return self.get_pages(self.key, self.page_count)
