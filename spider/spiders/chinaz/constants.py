import json

# GUID PING 测试站点列表
with open("config.json") as f:
    GUID_LIST = json.loads(f.read())["guid_list"]

# HEADERS
PING_HEADERS = {
    "cookie": "__gads=ID=1d541d1391ca8598-2205d6ab87cf0030:T=1640502483:RT=1640502483:S=ALNI_Mb4RggJ2FXUu2xMnpzhpZnUjzV94w; cz_statistics_visitor=638f9d6c-35df-efd7-95e1-4946df727e83; UM_distinctid=17ffc61186a268-0a6c9e8d376d3b-978183a-144000-17ffc61186b10c; qHistory=aHR0cDovL3BpbmcuY2hpbmF6LmNvbV9QaW5n5qOA5rWLfGh0dHA6Ly93aG9pcy5jaGluYXouY29tL19XaG9pc+afpeivonxodHRwOi8vdG9vbC5jaGluYXouY29tL2lwd2hvaXMvX0lQIFdIT0lT5p+l6K+ifGh0dHA6Ly9pcC50b29sLmNoaW5hei5jb20vaXBiYXRjaC9fSVDmibnph4/mn6Xor6J8aHR0cDovL3Nlby5jaGluYXouY29tX1NFT+e7vOWQiOafpeivonxodHRwOi8vdG9vbC5jaGluYXouY29tX+ermemVv+W3peWFt3xodHRwOi8vdG9vbC5jaGluYXouY29tL25zbG9va3VwL19uc2xvb2t1cOafpeivonxodHRwOi8vdG9vbC5jaGluYXouY29tL3Rvb2xzL3VybGVuY29kZS5hc3B4X1VybEVuY29kZee8lueggS/op6PnoIE=; Hm_lvt_aecc9715b0f5d5f7f34fba48a3c511d6=1650939469,1651126577; CNZZDATA5082706=cnzz_eid%3D19773035-1650931698-%26ntime%3D1651710854; Hm_lvt_ca96c3507ee04e182fb6d097cb2a1a4c=1649206696,1650939466,1651712813; Hm_lpvt_ca96c3507ee04e182fb6d097cb2a1a4c=1651713145",
    "origin": "https://ping.chinaz.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
}

# PING 测试数据字典模板
PING_DATA_TEMPLATES = {
    "guid": None,
    "host": None,
    "ishost": "0",
    "isipv6": "0",
    "encode": "xICuydcBeRPUGBWCA1jXoC|hgB1APvx2",
    "checktype": "0",
}

# PING 请求 URL
PING_URL = "https://ping.chinaz.com/iframe.ashx?t=ping&callback=jQuery111307360441126670261_1651713144552"

# PING 测试功能请求极限线程数量
PING_SEMAPHORE = 400
