from zbspider.spider import spider_run
from zbspider.mparser import parser_run
from zbspider.mode.sqlmanager import SQLManager
from zbspider.myemail import mail_to_user
import time

def mail_msg(data):
    td_html = ""
    for td in reversed(data):
        td_html += "<tr><td>"+td['title']+"</td><td>"\
            +td['link']+"</td><td>"+td['time']+"</td></tr>"
    html = """
    <table>
        <tr>
            <th>项目名称</th>
            <th>项目链接</th>
            <th>更新时间</th>
        </tr>"""+td_html+"""
    </table>
    """
    return html


if __name__ == '__main__':
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
    mail_message = mail_msg(results)
    mail_to_user(mail_message)
    # 若不存在： 获取下一页数据,补全列表，直到存在
    for result in reversed(results):
        # print(result)
        sql.insert(result)
    # 关闭数据库
    sql.close()