# 百度搜素 URL 模板
BAIDU_URL_MODEL = "https://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=def1c2ab00025382&ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baidu&wd={}&oq=csdn&rsv_pq=def1c2ab00025382&rsv_t=7f00gTGgKdY38cB6lCoXbj2pHu%2BRBSpcprcLKNjH7AC0JuinGdMzXi2MZRw&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t&bs=csdn&rsv_sid=undefined&_ss=1&clist=2f1030d0d96939aa&hsug=&f4s=1&csor=0&_cr1=26753&pn={}"

# 百度用 HEADERS
BAIDU_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'br',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'www.baidu.com',
    'Pragma': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Cookie': 'BIDUPSID=BDAB0F5750EB296F4ED7F9E3AAC0B43B; PSTM=1603455310; __yjs_duid=1_72558adbec0cffd7ca5cea5d8af88d701619686619619; BAIDUID=DE525E1A6F7780D06C9051891CCE2E53:FG=1; BD_UPN=12314753; sug=3; sugstore=1; ORIGIN=0; bdime=0; BDUSS=FXdHJnTkZiWGlYWU1BUmpxT2tJR0RMWWhGMGg3RENnRkFhVXNXWmVBTFMta3hpSVFBQUFBJCQAAAAAAQAAAAEAAADF3N89bHNwYWN0aW9uAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANJtJWLSbSViUE; BDUSS_BFESS=FXdHJnTkZiWGlYWU1BUmpxT2tJR0RMWWhGMGg3RENnRkFhVXNXWmVBTFMta3hpSVFBQUFBJCQAAAAAAQAAAAEAAADF3N89bHNwYWN0aW9uAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANJtJWLSbSViUE; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=SACOJexroG0xtr6DhqEPrZqOVCSeEhQTDYLEOPlhh2K5oJIVJeC6EG0Ptqxfx2P-EHtdogKK3gOTH4AF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR32Wn7a5TrDHJTg5DTjhPrM0PQmWMT-MTryKKJybP_-sbnlQq3KWR_g34bgKxQ3LGnRhlRNBMJSjbP4yTooyxFZyxomtfQxtNRJQ4nDMIomKq5S5-OobUPUDUJ9LUkJ0mcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-DK4e5_M3e; BDSFRCVID_BFESS=SACOJexroG0xtr6DhqEPrZqOVCSeEhQTDYLEOPlhh2K5oJIVJeC6EG0Ptqxfx2P-EHtdogKK3gOTH4AF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tR32Wn7a5TrDHJTg5DTjhPrM0PQmWMT-MTryKKJybP_-sbnlQq3KWR_g34bgKxQ3LGnRhlRNBMJSjbP4yTooyxFZyxomtfQxtNRJQ4nDMIomKq5S5-OobUPUDUJ9LUkJ0mcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-DK4e5_M3e; ab_sr=1.0.1_ZjEwOGE2OTU4MzYyZjFkNjIxNzk3OWViNWM3MWQxMWQ3NjUyNDg5MmM4ZmI2MTllZGNiMTA3NWY2MjY1Y2Q0YmFhNzkxOGE5ZjZiZDRkMTg3MmIxOTdmYTZhMjM2OWExOWI0ZjQxYzEwYzdjN2IwZDJlYWI2MDQ0OGM1ZTM3NzlhMDIxMmY2OTMwYTRmMTFhYTI5YTliZmMxNGRhMmJhYQ==; H_PS_PSSID=35838_36056_34812_36087_36166_34584_36075_35994_35955_35319_26350_36115_36101_36061; delPer=0; BD_CK_SAM=1; PSINO=6; channel=localhost:8888; COOKIE_SESSION=27_0_9_9_0_11_1_0_9_6_2_6_0_0_0_0_0_0_1648203711%7C9%2356838_13_1648090056%7C9; H_PS_645EC=d64fHzSP0y1iRigRl6veKcwyoBH9Q6PrHjJGwV62VpgyqvQuh42YE7q36Uk; BA_HECTOR=2h0l8g0g00ag8lago51h3r6v30q; baikeVisitId=63556072-7765-42a6-86b7-6f57ba9348f6',
}
