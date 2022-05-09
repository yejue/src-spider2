# 多源爬虫服务

## 一、开发环境

python3.10、ubuntu2204

（python 最低需要 python3.8）

**附注：本项目使用数据库为 sqlite3，路径为 /db.sqlite3**

## 二、快速启动

1. 安装所有依赖包，`pip install -r requirements.txt`
2. 进入 src-spider2 项目目录，创建 logs 文件目录。
3. 在 src-spider2 项目目录，使用下列命令启动服务。

```shell
$ python manage.py runserver 0:8000  

# 0 为可通过的 IP 反掩码，全写为 0.0.0.0
# 8000 为启动端口
```
3. 通过提供的接口获取数据或启动即时爬虫（非即时爬虫都采用命令启动）
4. 通过提供的爬虫任务命令更新或爬取数据
5. 通过提供的任务命令维护某些爬虫的 Cookie

## 三、接口设计

#### 3.1 百度搜索爬虫

接口地址：/spider/baidu-search/

返回格式：json

请求方式：get

请求示例： /spider/baidu-search/?key=清华&page_count=10

接口备注： 百度搜索调用接口，可传入两个参数，暂无过滤参数

------

参数说明：

| 名称       | 必须性 | 类型    | 描述                                   | 默认值 |
| ---------- | ------ | ------- | -------------------------------------- | ------ |
| key        | 是     | string  | 搜索关键词，可以由多个词组成，支持空格 | 无     |
| page_count | 否     | integer | 需要爬取的搜索结果页数                 | 10     |

返回参数说明：

| 名称        | 类型   | 说明                         |
| ----------- | ------ | ---------------------------- |
| result_code | string | 返回状态码                   |
| message     | string | 状态码对应信息，或自定义信息 |
| data        | list   | 搜索结果数据列表             |

返回参数示例：

```json
{
    "data": [
        {"title": "清华大学", "url": "https://www.tsinghua.edu.cn/"}
    ],
    "message": "成功",
    "result_code": "200"
}
```

#### 3.2 谷歌搜索爬虫

接口地址：/spider/google-search/

返回格式：json

请求方式：get

请求示例： /spider/google-search/?key=清华&page_count=10

接口备注： 谷歌搜索调用接口，可传入两个参数，暂无过滤参数。谷歌爬虫需要使用代理，当前代理协议为 SOCKS，默认请求代理端口为 10808。

------

参数说明：

| 名称       | 必须性 | 类型    | 描述                                   | 默认值 |
| ---------- | ------ | ------- | -------------------------------------- | ------ |
| key        | 是     | string  | 搜索关键词，可以由多个词组成，支持空格 | 无     |
| page_count | 否     | integer | 需要爬取的搜索结果页数                 | 10     |

返回参数说明：

| 名称        | 类型   | 说明                         |
| ----------- | ------ | ---------------------------- |
| result_code | string | 返回状态码                   |
| message     | string | 状态码对应信息，或自定义信息 |
| data        | list   | 搜索结果数据列表             |

返回参数示例：

```json
{
    "data": [
        {"title": "清华大学", "url": "https://www.tsinghua.edu.cn/"}
    ],
    "message": "成功",
    "result_code": "200"
}
```

#### 3.3 补天&漏洞盒子信息列表

接口地址：/api/bt-vulbox/

返回格式：json

请求方式：get

请求示例： /api/bt-vulbox/?page=1&limit=25

接口备注： 补天和漏洞盒子信息展示接口。可使用 page 和 limit 参数进行结果过滤。（支持使用表字段进行结果过滤）

------

参数说明：

| 名称  | 必须性 | 类型    | 描述                            | 默认值 |
| ----- | ------ | ------- | ------------------------------- | ------ |
| page  | 否     | integer | 请求结果的页数，缺省为 1        | 1      |
| limit | 否     | integer | 每页需要展示的结果数量，默认 25 | 25     |

返回参数说明：

| 名称        | 类型    | 说明                         |
| ----------- | ------- | ---------------------------- |
| result_code | string  | 返回状态码                   |
| message     | string  | 状态码对应信息，或自定义信息 |
| data        | list    | 搜索结果数据列表             |
| total_count | integer | 总的结果数量                 |

返回参数示例：

关于 data 内的字段介绍参照 **6.1数据表模型**

```json
{
    "data": [
        {
            "id": 1,
            "company_name": "乐信集团安全应急响应中心",
            "test_range": "",
            "property_range": "\n资产\n\n适用范围...",
            "origin": "漏洞盒子",
            "origin_url": "https://lxsrc.vulbox.com",
        }
    ],
    "total_count": 78,
    "message": "成功",
    "result_code": "200"
}
```

#### 3.4 补天&漏洞盒子详情接口

接口地址：/api/bt-vulbox/:id

返回格式：json

请求方式：get

请求示例： /api/bt-vulbox/1/

接口备注： 补天和漏洞盒子信息详情接口。可使用 id 查询某一条目详情。暂无过滤参数。

------

参数说明：

| 名称 | 必须性 | 类型    | 描述          | 默认值 |
| ---- | ------ | ------- | ------------- | ------ |
| id   | 是     | integer | 数据库中的 id |        |

返回参数说明：

| 名称        | 类型   | 说明                         |
| ----------- | ------ | ---------------------------- |
| result_code | string | 返回状态码                   |
| message     | string | 状态码对应信息，或自定义信息 |
| data        | list   | 搜索结果数据列表             |

返回参数示例：

关于 data 内的字段介绍参照 **6.1数据表模型**

```json
{
    "data": [
        {
            "id": 1,
            "company_name": "乐信集团安全应急响应中心",
            "test_range": "",
            "property_range": "\n资产\n\n适用范围...",
            "origin": "漏洞盒子",
            "origin_url": "https://lxsrc.vulbox.com",
        }
    ],
    "message": "成功",
    "result_code": "200"
}
```

#### 3.5 潮汐在线指纹识别搜索爬虫

接口地址：/spider/td-search/

返回格式：json

请求方式：get

请求示例： /spider/td-search/?domain=baidu.com

接口备注： 潮汐在线指纹识别搜索爬虫，可传入一个参数，暂无过滤参数。

------

参数说明：

| 名称   | 必须性 | 类型   | 描述 | 默认值 |
| ------ | ------ | ------ | ---- | ------ |
| domain | 是     | string | 域名 | 无     |

返回参数说明：

| 名称        | 类型   | 说明                         |
| ----------- | ------ | ---------------------------- |
| result_code | string | 返回状态码                   |
| message     | string | 状态码对应信息，或自定义信息 |
| data        | dict   | 搜索结果数据字典             |

data 数据说明:

data 数据按照源数据格式返回，下列返回示例严格遵循 JSON 规范，故省略类型说明。

| 参数            | 描述                                                         |
| --------------- | ------------------------------------------------------------ |
| url             | url                                                          |
| title           | 目标网站标题                                                 |
| middleware      | 中间件。在此表示反向代理引擎（NGINX 等）                     |
| cms             | cms 信息                                                     |
| banner          | banner 信息                                                  |
| ip_message      | ip 信息，包含ip，ISP机房信息，地址，GPS信息                  |
| cdn             | CDN 信息                                                     |
| os              | 操作系统信息                                                 |
| domain_msg      | 域名信息。包含域名注册商，whois 服务器，域名注册与过期时间等 |
| domain_register | 域名注册商                                                   |
| whois_server    | whois 服务器                                                 |
| domain_reg_date | 域名注册时间                                                 |
| domain_exp_date | 域名过期时间                                                 |
| name_servers    | DNS 服务器列表                                               |
| domain_record   | 域名备案信息                                                 |
| property        | 备案性质，个人或者企业                                       |
| number          | 备案号                                                       |
| title           | 备案标题                                                     |

返回参数示例：

```json
{
    "result_code": "200", 
    "message": "成功", 
    "data": {
        "url": "http://baidu.com", 
        "title": "", 
        "middleware": "Apache",
        "cms": [], 
        "banner": {
            "URL Redirect": [
                "http_status:200, Title:百度一下，你就知道, IP:110.242.68.4, HTTPServer:BWS/1.1", 
                "http_status:200, Title:百度一下，你就知道, IP:110.242.68.4, HTTPServer:Apache"
            ]
        }, 
        "ip_message": {
            "ip": "220.181.38.148", 
            "isp": "电信IDC机房", 
            "area": "北京市", 
            "gps": "116.40387397,39.91488908"
        }, 
        "cdn": {"cdn": "UnKownCdn", "cdn_cname": ""}, 
        "os": "Linux", 
        "domain_msg": {
            "domain_register": "MarkMonitor, Inc.", 
            "whois_server": "whois.markmonitor.com", 
            "domain_reg_date": [
                "1999, 10, 11, 11, 5, 17", 
                "1999, 10, 11, 11, 5, 17, tzinfo=datetime.timezone.utc"
            ], 
            "domain_exp_date": [
                "2026, 10, 11, 11, 5, 17",
                "2026, 10, 11, 7, 0, tzinfo=datetime.timezone.utc"
            ], 
            "name_servers": [
                "NS1.BAIDU.COM", 
                "NS2.BAIDU.COM", 
                "NS3.BAIDU.COM", 
                "NS4.BAIDU.COM", 
                "NS7.BAIDU.COM", 
                "ns2.baidu.com", 
                "ns3.baidu.com", 
                "ns7.baidu.com", 
                "ns4.baidu.com", 
                "ns1.baidu.com"
            ], 
            "emails": [
                "abusecomplaints@markmonitor.com", 
                "whoisrequest@markmonitor.com"
            ], 
            "state": "Beijing"
        }, 
        "domain_record": {
            "company": "北京百度网讯科技有限公司", 
            "property": "企业", 
            "number": "", 
            "title": "百度", 
            "time": "2022-03-11"
        }
    }
}
```

#### 3.6 站长之家 PING 节点搜索爬虫

接口地址：/spider/chinaz-search/

返回格式：json

请求方式：get

请求示例：/spider/chinaz-search/?domain=baidu.com

接口备注：站长之家 PING 节点搜索爬虫，可传入一个参数，暂无过滤参数。

------

参数说明：

| 名称   | 必须性 | 类型   | 描述 | 默认值 |
| ------ | ------ | ------ | ---- | ------ |
| domain | 是     | string | 域名 | 无     |

返回参数说明：

| 名称        | 类型   | 说明                         |
| ----------- | ------ | ---------------------------- |
| result_code | string | 返回状态码                   |
| message     | string | 状态码对应信息，或自定义信息 |
| data        | list   | 搜索结果数据列表             |

data 参数说明：

| 名称     | 类型     | 说明           |
| -------- | -------- | -------------- |
| ip_list  | list     | 所有响应 ip    |
| ip_count | interger | ip_list 的个数 |

返回参数示例：

```json
{
    "result_code": "200",
    "message": "成功",
    "data": {
        "ip_list": [
            "220.181.38.251",
            "220.181.38.148"
        ],
        "ip_count": 2
    }
}
```

#### 

## 四、暂定错误码

| 错误码 | 描述                                           |
| ------ | ---------------------------------------------- |
| 200    | OK                                             |
| 4001   | PARAM_ERR 传入的参数值错误，多出现于值类型错误 |
| -1     | UNKNOWN_ERR 未知错误                           |
| 5001   | CONNECT_ERR 连接错误，多出现为代理连接异常     |

## 五、爬虫任务
1. 补天和漏洞盒子数据获取任务

   `python manage.py runbtvulbox`
   
3. 潮汐在线指纹识别爬虫 Cookie 维护任务（建议 30 分钟维护一次）

   `python manage.py maintainTdCookie`

## 六、补天&漏洞盒子爬虫描述
### 6.1 数据表模型

| 字段名         | 类型   | 描述                                               | 默认 |
| -------------- | ------ | -------------------------------------------------- | ---- |
| company_name   | string | 公司名                                             |      |
| test_range     | string | 漏洞测试范围。长文本，一般是补天漏洞平台才有的字段 |      |
| collect_range  | string | 漏洞收集范围。暂未使用，类型为长文本               |      |
| property_range | string | 资产范围，即”资产“。长文本。一般是漏洞盒子的字段   |      |
| origin         | string | 来源。漏洞盒子或者补天                             |      |
| origin_url     | string | 来源地址。即采集的地址                             |      |

```python
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
        ordering = ["id"]
        verbose_name = "补天&漏洞盒子信息表"
        verbose_name_plural = "补天&漏洞盒子信息表"
```

### 6.2 数据采集任务

1. 使用命令 `python manage.py runbtvulbox` 启动爬虫服务，在 /logs/spider.log 中查看爬虫运行日志