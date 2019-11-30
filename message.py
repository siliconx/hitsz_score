import smtplib
from email.message import EmailMessage

# 第三方 SMTP 服务
mail_host='smtp.qq.com'  # 设置smtp服务器
mail_user='abc@qq.com'  # 发送邮箱
mail_pass='xxx'  # 客户端授权码, 非普通登录密码

sender = mail_user
receivers = ['xxx@163.com']  # 接收邮箱

def send(text):
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = '您有新的成绩！'
    msg['From'] = sender
    msg['To'] = receivers

    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(mail_host, 25)
        smtp_obj.login(mail_user, mail_pass)
        smtp_obj.send_message(msg)
        smtp_obj.quit()
        print("邮件发送成功")
        return True
    except smtplib.SMTPException as e:
        print(e)
        return False

