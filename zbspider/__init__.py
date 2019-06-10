"""
招标网爬虫主模块
功能：
整合四个子功能模块
"""

class ZBSpider(object):
    """
    主程序类
    """

    def __init__(self,config):
        self.config = config

    def run():
        # 开启数据库控制
        sql = SQLManager()
        # 查询最后一个数据
        last_one_title = sql.get_last_one_title()
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
                time.sleep(120)
        mail_to_user(results)
        # 若不存在： 获取下一页数据,补全列表，直到存在
        for result in reversed(results):
            # print(result)
            sql.insert(result)
        # 关闭数据库
        sql.close()