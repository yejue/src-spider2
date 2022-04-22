import logging

from django.core.management import BaseCommand

from spider.spiders import BtAndVulBoxMsgSpider
from apps.spider.models import BtAndVulBoxModel


logger = logging.getLogger("spider")  # 爬虫日志器


class Command(BaseCommand):
    """命令处理类
      1. 向补天漏洞盒子表写入数据
      2. 在 1 的基础上个更新数据
    """

    def handle(self, *args, **options):
        spider = BtAndVulBoxMsgSpider()
        res_list = spider.run_all_mission()

        for item in res_list:
            print(item)
            queryset = BtAndVulBoxModel.objects.filter(company_name=item["company_name"], origin=item["origin"])
            if queryset:
                queryset.update(**item)
            else:
                queryset.create(**item)

        print(f"补天&漏洞盒子爬虫任务完成")
        logger.info(f"补天&漏洞盒子爬虫任务完成")
