from django.db import models
from libs.models import BaseModel
# Create your models here.


class BtAndVulBoxModel(BaseModel):
    """补天&漏洞盒子信息表"""
    company_name = models.CharField("公司名", max_length=50, help_text="公司名")
    test_range = models.TextField("漏洞测试范围", help_text="漏洞测试范围", null=True)
    collect_range = models.TextField("漏洞收集范围", help_text="漏洞收集范围", null=True)
    property_range = models.TextField("资产范围", help_text="资产范围", null=True)

    origin = models.CharField("信息来源", max_length=50, help_text="信息来源", null=True)
    origin_url = models.URLField("来源地址", help_text="来源地址", null=True)

    def __str__(self):
        return f"<{self.company_name}:{self.origin}>"

    class Meta:
        db_table = "bt_vulbox_table"
        verbose_name = "补天&漏洞盒子信息表"
        verbose_name_plural = "补天&漏洞盒子信息表"
