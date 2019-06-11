import requests
import random

class Spider(object):
    """
    网络爬虫类基类
    
    功能：获取网站上的数据
    """

    def __init__(self, url, params, headers, cookies):
        self.url = url
        self.params = params
        self.headers = headers
        self.cookies = cookies

    def get(self, page=1):
        self.params['page'] = page
        try:
            web = requests.get(self.url, params=self.params, headers=self.headers, cookies=self.cookies)
        except ConnectionResetError:
            print("ERROR: 远程主机强迫关闭了一个现有的连接,重试!")
            web = requests.get(self.url, params=self.params, headers=self.headers, cookies=self.cookies)
        return web.text