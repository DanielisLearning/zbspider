"""
配置文件
"""
import os
# 根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config():
    """基础配置"""
    # 数据库位置
    DATABASE = os.path.join(BASE_DIR, "database/sqlite.db")
    # email 配置
    EMAIL = {
        'host':'smtp.fjiti.com',
        'user':'xf@fjiti.com',
        'pass':'hegexinfu123',
        'sender':'xf@fjiti.com',
        'receivers':'grq@fjiti.com'
    }
    SPIDER = []
    # 爬取页面
    URL = "https://www.zbytb.com/zb/search.php"
    # 头信息
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
        #"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    }
    # 缓存信息
    COOKIES = {
        "__jsluid": "47ac0b2fb3da3c3fcad6b1b43e554953",
        "UM_distinctid": "16a8ff56aacf9-068f97e3d7ae4b-3b654406-13c680-16a8ff56aad2b1",
        "Du4_vi-ds": "7bf0b180a6b50479fa5c0a69cad839ae",
        "CNZZDATA1271464574": "254670458-1557192656-https%253A%252F%252Ffzgp.zbytb.com%252F%7C1557192656",
        "Hm_lvt_47b9a4b804f6b4f81affae66cb8a57e9": "1557193387,1557196640",
        "Du4_last_search": "1557196801",
        "PHPSESSID": "sal1nv47767ufcm3uopl0bha63",
        "Hm_lpvt_47b9a4b804f6b4f81affae66cb8a57e9": "1557196841",
    }
    # 参数
    PARAMS = {
        "kw": "",
        "catid": 0,
        "areaid": 14,
        "page":0,
    }