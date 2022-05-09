import re
import asyncio
import aiohttp

from . import constants


class ChinaZPingSpider:
    """站长之家 PING 测试功能爬虫"""
    guid_list = constants.GUID_LIST
    ping_url = constants.PING_URL
    headers = constants.PING_HEADERS

    def __init__(self, domain):
        self.domain = domain

        # 设置 PING 测试载荷
        temp = constants.PING_DATA_TEMPLATES
        temp["host"] = self.domain
        self.ping_data = temp

    async def get_ping_one(self, data, semaphore):
        """异步获取一个 PING 测试结果"""
        async with semaphore:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.ping_url, headers=self.headers, data=data) as resp:
                    res = await resp.text()  # 异步等待站长之家响应
                    try:
                        ip = re.findall("ip:'(.*?)',", res)[0]
                    except IndexError:
                        return None
        return ip

    async def get_ping_all(self):
        """异步获取所有 PING 测试结果"""
        semaphore = asyncio.Semaphore(constants.PING_SEMAPHORE)  # 设置极限异步线程数量

        task_list = []  # 爬虫任务列表

        for g in self.guid_list:  # 使用每一个 GUID 创建一个异步任务
            temp_data = self.ping_data.copy()
            temp_data["guid"] = g
            task = asyncio.create_task(self.get_ping_one(temp_data, semaphore))
            task_list.append(task)

        done, _ = await asyncio.wait(task_list)

        # 过滤重复 IP
        ip_set = set()

        for i in done:
            if i.result():
                ip_set.add(i.result())

        # 格式化将要返回的数据
        data = {
            "ip_list": list(ip_set),
            "ip_count": len(ip_set)
        }

        return data

    def run(self):
        """爬虫开启"""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        res = loop.run_until_complete(self.get_ping_all())
        return res
