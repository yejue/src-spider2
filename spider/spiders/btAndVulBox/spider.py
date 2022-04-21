import re
import json
import requests

from bs4 import BeautifulSoup
from . import constants


class BtAndVulBoxMsgSpider:
    """补天&漏洞盒子信息爬虫"""
    bt_headers = constants.BT_HEADERS
    bt_corps_url = constants.BUTIAN_CORPS_URL

    vul_box_headers = constants.VULBOX_HEADERS
    vul_box_d_headers = constants.VULBOX_DETAIL_HEADERS
    vul_box_corps_url = constants.VULBOX_CORPS_URL

    def get_bt_list(self):
        """补天信息获取"""
        payload = {"s": 1, "p": 1, "sort": 1}
        req = requests.post(self.bt_corps_url, headers=self.bt_headers, data=payload)
        res = json.loads(req.content.decode("utf8"))
        return res["data"]["list"]

    def get_bt_detail(self, detail_url):
        """补天详情页信息获取"""
        req = requests.get(detail_url, headers=self.bt_headers, verify=False)

        if req.history:  # 重定向
            try:
                detail_url = req.history[1].headers["Location"]
            except IndexError:
                detail_url = req.history[0].headers["Location"]
            req = requests.get(detail_url, headers=self.bt_headers, verify=False)

        soup = BeautifulSoup(req.content.decode("utf8"), "html.parser")

        test_range = soup.select_one("#testRange").text
        test_range = re.sub(r"<.*?>", "\n", test_range)  # 格式化不规范的文本

        data = {
            "test_range": test_range,
        }
        return data

    def run_bt_mission(self):
        """补天信息获取总任务"""
        res_list = []  # 最终返回数据列表
        bt_list = self.get_bt_list()

        for item in bt_list:
            company_id = item["company_id"]
            url = constants.BUTIAN_PER_COMPANY_MODEL.format(company_id)  # 组合路径
            print(url)

            temp = {
                "company_name": item["company_name"],
                "origin": "补天漏洞响应平台",
                "origin_url": url
            }

            detail = self.get_bt_detail(url)  # 获取详情页内容
            temp.update(detail)
            res_list.append(temp)

        return res_list

    def get_vul_box_list(self):
        """获取漏洞盒子 SRC 列表"""
        req = requests.get(self.vul_box_corps_url, headers=self.vul_box_headers)
        res = json.loads(req.content.decode("utf8"))
        return res["data"]["list"]

    def get_vul_box_detail(self, detail_url):
        """获取漏洞盒子厂商详情页内容"""
        req = requests.get(detail_url, headers=self.vul_box_d_headers)
        soup = BeautifulSoup(req.content.decode("utf8"), "html.parser")
        property_ = soup.select_one(".ncec-main-net")
        property_ = property_.text if property_ else None
        return property_

    def run_vb_mission(self):
        """漏洞盒子数据获取任务"""
        res_list = []  # 最终返回数据列表
        corps_list = self.get_vul_box_list()

        for item in corps_list:
            detail_url = item["url"]
            print(detail_url)
            if "https" not in detail_url:
                detail_url = detail_url.replace("http", "https")

            property_ = self.get_vul_box_detail(detail_url)

            temp = {
                "company_name": item["task_title"],
                "origin": "漏洞盒子",
                "origin_url": detail_url,
                "property": property_,
            }
            res_list.append(temp)

        return res_list

    def run_all_mission(self):
        mission_list = [self.run_vb_mission, self.run_bt_mission]
        res_list = []

        for mission in mission_list:
            temp = mission()
            res_list.append(temp)
        return res_list
