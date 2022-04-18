import datetime

# 谷歌搜索 URL 模板
GOOGLE_URL_MODEL = "https://www.google.com.hk/search?q={}&newwindow=1&hl=zh-CN&start={}"

# 谷歌请求头
ck_time = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H")  # UTC时间，谷歌请求头格式
GOOGLE_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': f'1P_JAR={ck_time}; AEC=AVQQ_LAk1VLnq3geFQgjmb_-svWlMeKfYwnAMB7SkiKqFQnVbiH6n1BTHZM; NID=511=JxJGRq8g42aDhF5baQLGuRj6qhQ_xh8197o0Y3zcE07KenTzQzFQasvHuyGY-mHdzGSe-CvCRhnKQAtwQrTxWsUxBdqe2yY0mkOIRGJUA6Rkz9a-CtjiLJQCXL6IDg3XCNWViy8W8X0oShgvTBj9WZYQC0Dx_EOD_PrWyPRaGW2etBib0zqPik62KwLwckRevUqFA-Tj; DV=QyKbzY4ax3sv0J-HU_sc0ecCyrQz_Zf9oYQs_p7gZQMAAAA',
    'pragma': 'no-cache',
    'referer': 'https://www.google.com.hk/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"96.0.4664.45"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
}

# 代理
PROXIES = {
    "http": "socks5://127.0.0.1:10808",
    "https": "socks5://127.0.0.1:10808"
}
