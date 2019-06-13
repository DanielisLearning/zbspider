"""
邮件模块

用途：将查询到的结果通过邮件发送到关键用户
"""
from .myemail import mail_msg, mail_content
import smtplib

# 第三方 SMTP 服务
MAIL_HOST = "smtp.fjiti.com"
MAIL_USER = "xf@fjiti.com"
MAIL_PASS = "hegexinfu123"
SENDER = 'xf@fjiti.com'
RECEIVERS = ['grq@fjiti.com']


def mail_to_user(mail, text):
    # 生成邮件的内容
    msg = mail_content(mail['sender'], mail['receivers'], mail_msg(text))
    # 发送邮件
    server = smtplib.SMTP(mail['host'], 25)
    # server.set_debuglevel(1)
    server.login(mail['user'], mail['pass'])
    server.sendmail(mail['sender'], mail['receivers'], msg.as_string())
    server.quit()
