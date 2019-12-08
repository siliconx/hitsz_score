import smtplib
from email.message import EmailMessage
import config

# 第三方 SMTP 服务
mail_host = config.EMAIL_HOST
mail_user = config.EMAIL_USERNAME
mail_pass = config.EMAIL_PASSWORD

sender = mail_user
receivers = config.EMAIL_RECEIVERS

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

