import logging

from django.core.management import BaseCommand
from spider.spiders import TdFingerSearchSpider

logger = logging.getLogger("spider")  # 爬虫日志器


class Command(BaseCommand):
    """潮汐在线指纹识别 Cookie 维护"""

    def handle(self, *args, **options):
        domain = "baidu.com"
        spider = TdFingerSearchSpider(domain)
        res = spider.get_finger_data()

        if not res:
            print("Cookie 维护失败，该 Cookie 已提前过期")
            logger.info("Cookie 维护失败，该 Cookie 已提前过期")
        else:
            print("Cookie 维护完成")
            logger.info("Cookie 维护完成")
