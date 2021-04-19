import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

sender = 'ab@bg.com'
# 开通邮箱服务后，设置的客户端授权密码
pwd = 'ai'
# 接收邮件，可设置为你的邮箱
receivers = ['lyz@163.com']

msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("邮件测试", 'utf-8')
msgRoot['To'] = Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
msgRoot['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="https://www.python.org">Python官方网站</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('1.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

try:
    # 使用非本地服务器，需要建立ssl连接
    smtpObj = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
    smtpObj.login(sender, pwd)
    smtpObj.sendmail(sender, receivers, msgRoot.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as se:
    print(f"Error: 无法发送邮件.Case:{se}")
