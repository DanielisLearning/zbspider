"""
招标网爬虫主模块
功能：
整合四个子功能模块
"""
from .mode.sqlmanager import SQLManager
from .spider import spider_run, Spider
from .mparser import parser_run
from .myemail import mail_to_user
import time

class ZBSpider(object):
    """
    主程序类
    """

    def __init__(self,config):
        self.config = config
        self.sql = SQLManager(self.config.DATABASE)
        self.spider = Spider(self.config.URL, self.config.PARAMS, self.config.HEADERS, self.config.COOKIES)

    def run(self):
        # 查询最后一个数据
        last_one_title = self.sql.get_last_one_title()
        # 建立results列表
        results = []
        page = 1
        while True:
            # 检查数据是否在列表中存在
            if last_one_title in results:
                # 若存在： 按顺序分割列表，将顺序后的数据存入数据库
                print("存在")
                # print(results)
                index = results.index(last_one_title)
                results = results[:(index - 1)]
                # print(results)
                break
            else:
                print("不存在%d" %(page))
                # 爬取网页
                html_doc = spider_run(page)
                # 分析网页，获得结果
                results += parser_run(html_doc)
                # print(results)
                page = page + 1
                time.sleep(56)
        mail_to_user(results)
        # 若不存在： 获取下一页数据,补全列表，直到存在
        for result in reversed(results):
            # print(result)
            self.sql.insert(result)
        # 关闭数据库
        self.sql.close()