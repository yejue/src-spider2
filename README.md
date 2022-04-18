# 多源爬虫服务

## 一、开发环境

python3.10、ubuntu2204

## 二、快速启动

1. 安装所有依赖包，`pip install -r requirements.txt`
2. 进入 src-spider2 项目目录，使用下列命令启动服务。

```shell
$ python manage.py runserver 0:8000  

# 0 为可通过的 IP 反掩码，全写为 0.0.0.0
# 8000 为启动端口
```

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
    data: [
        {title: "清华大学", url: "https://www.tsinghua.edu.cn/"}
    ],
    message: "成功",
    result_code: "200"
}
```

#### 3.2 谷歌搜索爬虫

接口地址：/spider/google-search/

返回格式：json

请求方式：get

请求示例： /spider/google-search/?key=清华&page_count=10

接口备注： 谷歌搜索调用接口，可传入两个参数，暂无过滤参数

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
    data: [
        {title: "清华大学", url: "https://www.tsinghua.edu.cn/"}
    ],
    message: "成功",
    result_code: "200"
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

