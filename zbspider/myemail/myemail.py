"""
此模块两个函数，分别用于Email发送与Email内容构造
"""
from email.header import Header
from email.mime.text import MIMEText


# 邮件中的HTML内容
# TODO: html下time列的修改
def mail_msg(text):
    td_html = ""
    for data in reversed(text):
        td_html += "<tr><td><a href=\"" + data['link'] + "\">" + data['title'] + "</a></td><td>"\
            + data['time'] + "</td></tr>"
    html = """
    <table>
        <tr>
            <th>项目名称</th>
            <th>更新时间</th>
        </tr>""" + td_html + """
    </table>
    """
    return html


# 邮件格式内容
def mail_content(sender, receiver, text):
    msg = MIMEText(text, 'html', 'utf-8')
    msg['From'] = "福建省和格信息技术服务有限公司" + sender
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header('中国采购招标网采购结果', 'utf-8').encode()
    return msg
