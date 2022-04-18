import requests
import time
import random

from bs4 import BeautifulSoup
from . import constants


class GoogleSearchSpider:
    """谷歌搜索爬虫"""
    url_model = constants.GOOGLE_URL_MODEL
    headers = constants.GOOGLE_HEADERS

    def __init__(self, key, page_count=10, is_log=True):
        self.key = key
        self.page_count = page_count
        self.is_log = is_log

        self.session = requests.Session()
        self.session.get("https://www.google.com.hk/", verify=False, proxies=constants.PROXIES)  # 初次访问模拟

    def get_page(self, key, n):
        """取第 n 页"""
        res = []

        url = self.url_model.format(key, n)
        req = self.session.get(url, headers=self.headers, proxies=constants.PROXIES)
        data = req.content.decode("utf8")  # 页面资源

        soup = BeautifulSoup(data, "html.parser")  # BS 筛选对象
        soup_temp = soup.select(".yuRUbf")  # 筛选页面所有词条

        for item in soup_temp:
            title = item.select_one("h3").text
            target_url = item.select_one("a").attrs["href"]
            res.append({"title": title, "url": target_url})

        return res

    def get_pages(self, key, page_count):
        """取 n 页"""
        res = []

        for i in range(1, page_count+1):
            temp = self.get_page(key, i)

            if self.is_log:
                print(f"[{i}] - 获取数量：{len(temp)}")

            res.extend(temp)
            time.sleep(random.randint(1, 10)/10)  # 缓冲时间
        return res

    def run(self):
        """自主爬行任务"""
        return self.get_pages(self.key, self.page_count)
