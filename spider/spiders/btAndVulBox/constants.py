# 补天专属SRC URL
BUTIAN_CORPS_URL = "https://www.butian.net/Reward/corps"
BUTIAN_PER_COMPANY_MODEL = "https://www.butian.net/Company/{}"

# 漏洞盒子企业 SRC 列表
VULBOX_URL = "https://www.vulbox.com/projects/list"
VULBOX_CORPS_URL = "https://vbapi.vulbox.com/v1/task/getList?page=1&task_type=3&limit=9999"

# 基础 HEADERS
BASE_HEADERS = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
}

# 补天 HEADERS
BT_HEADERS = BASE_HEADERS
BT_HEADERS.update({
    "Cookie": "btuc_ba52447ea424004a7da412b344e5e41a=e7617e7f2f12fa42c592ecb6dcdadca620f41f12eac6559980e7a47982944b0b; PHPSESSID=1dfalr1kldjagbk6bh0tdhvdv2; _currentUrl_=%2FMessage",
})

# 漏洞盒子 HEADERS
VULBOX_HEADERS = BASE_HEADERS
VULBOX_HEADERS.update({
    "vulbox-key": "d85f3fa7a10ad5cb46d62fa6b32c936c_tTkecuhZESPNc4f5bcCZPvJ+8/B/CLbFNd57CtNyTfNcJ7bcgAUOiwp/vSN9IkB7"
})

# 漏洞盒子跨域 HEADERS
VULBOX_DETAIL_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "Key_auth=vHgjy%2FMTms9aGQnI5Pv2CmEX2zrsFQfixnA7608iOUw%3D; VulBox_uid=tTkecuhZESPNc4f5bcCZPvJ%2B8%2FB%2FCLbFNd57CtNyTfNcJ7bcgAUOiwp%2FvSN9IkB7; authorization=1; vulbox_key=d85f3fa7a10ad5cb46d62fa6b32c936c_tTkecuhZESPNc4f5bcCZPvJ%2B8%2FB%2FCLbFNd57CtNyTfNcJ7bcgAUOiwp%2FvSN9IkB7; hacker_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NTAzMzEzOTEsImV4cCI6MTY1MDkzNjE5MSwidXNlcl9pZCI6IjM5NzAyMSIsInJvbGVfaWQiOjAsInVzZXJfbmFtZSI6InllanVlMSJ9.ha027Y2_lT-FNHKZlDiTPgb7roA8rr0ZeJXlRXkr2GA; Hm_lvt_8dd9d540bb282c90af2121009e254daa=1650331111,1650417101; PHPSESSID=e38dql9gvtpj3hli2pv70jctj6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221803f6652b33b5-0b2d767a80d987-978183a-1327104-1803f6652b4526%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22http%3A%2F%2Flocalhost%3A8888%2F%22%7D%2C%22%24device_id%22%3A%221803f6652b33b5-0b2d767a80d987-978183a-1327104-1803f6652b4526%22%7D; Hm_lvt_ca048dd0dbb114747cc58907f7e20022=1650502202; Hm_lpvt_ca048dd0dbb114747cc58907f7e20022=1650502202; Hm_lpvt_8dd9d540bb282c90af2121009e254daa=1650502205",
}

