import requests


class Spider(object):
    """
    网络爬虫类基类

    功能：获取网站上的数据
    """

    def __init__(self, url, **kwargs):
        self.url = url
        self.kwargs = kwargs

    def get(self, page=1):
        self.kwargs['params']['page'] = page
        while True:
            try:
                web = requests.request('GET', self.url, **self.kwargs)
                break
            except ConnectionResetError:
                print("ERROR: 远程主机强迫关闭了一个现有的连接,重试!")
        return web.text
