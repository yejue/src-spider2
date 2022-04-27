import json
import requests

from . import constants


class TdFingerSearchSpider:
    """TideFinger 网站指纹识别爬虫"""

    td_headers = constants.TD_HEADERS
    td_url = constants.TD_FINGER_URL

    def __init__(self, target):
        self.target = target

    def get_finger_data(self):
        """获取指纹识别信息"""
        data = {"target": self.target}
        req = requests.post(self.td_url, headers=self.td_headers, data=data)
        res = json.loads(req.content.decode("utf8"))
        if res["status"] == 2:
            print("Cookie 失效，请重新设置")
            return 0
        else:
            res = res["res"]

        # 筛选需要的信息重组 res
        temp_dict = {
            "url": res["url"],
            "title": json.loads(res["finger"])["title"],  # 网站标题
            "middleware": json.loads(res["finger"])["httpserver"],  # 中间件
            "cms": res["cms"],  # CMS 信息
            "banner": res["banner"],  # Banner 信息

            "ip_message": {  # IP 地址信息
                "ip": res["ip"],
                "isp": json.loads(res["ip_gps_info"])["isp"],
                "area": json.loads(res["ip_gps_info"])["area"],
                "gps": json.loads(res["ip_gps_info"])["gps"],
            },

            "cdn": res["cdn"],  # CDN 信息
            "os": res["os"],  # 操作系统信息

            "domain_msg": {  # 域名信息
                "domain_register": json.loads(res["domain_whois"])["reg"],  # 域名注册商
                "whois_server": json.loads(res["domain_whois"])["whois_server"],  # whois 服务器
                "domain_reg_date": json.loads(res["domain_whois"])["creation_date"],  # 域名注册时间
                "domain_exp_date": json.loads(res["domain_whois"])["expiration_date"],  # 域名过期时间
                "name_servers": json.loads(res["domain_whois"])["name_servers"],  # DNS 服务器
                "emails": json.loads(res["domain_whois"])["emails"],  # 注册邮箱
                "state": json.loads(res["domain_whois"])["state"],  # 注册人地址
            },

            "domain_record": {  # 域名备案信息
                "company": json.loads(res["domain_beian"])["gongsi"],  # 备案主体
                "property": json.loads(res["domain_beian"])["xingzhi"],  # 备案性质
                "number": json.loads(res["domain_beian"])["beian"],  # 备案号
                "title": json.loads(res["domain_beian"])["title"],  # 备案标题
                "time": json.loads(res["domain_beian"])["time"],  # 备案时间
            }
        }

        return temp_dict
