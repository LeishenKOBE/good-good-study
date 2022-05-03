import smtplib
from email.mime.text import MIMEText
from email.header import Header

text = '''亲爱的学员，你好！
​    我是吴枫老师，能遇见你很开心。
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''

msg = MIMEText(text, 'plain', 'utf-8')

msg['From'] = Header('许嵩')
msg['To'] = Header('石东昭')
msg['Subject'] = Header('粉丝')

username = 'wuyujiesong@163.com'
password = 'BWHOFHDEHSRMFJAC'

server = smtplib.SMTP()


server.connect('smtp.163.com', 25)
server.login(username, password)

server.sendmail(username, '963954711@qq.com', msg.as_string())
server.quit()
