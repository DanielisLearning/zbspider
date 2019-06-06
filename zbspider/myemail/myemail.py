"""
此模块两个函数，分别用于Email发送与Email内容构造
"""
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 邮件内容
def mail_content(sender, receiver, text):
    msg = MIMEText(text, 'html', 'utf-8')
    msg['From'] = sender
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header('中国采购招标网采购结果', 'utf-8').encode()
    return msg
