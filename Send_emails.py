#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '13799403094@163.com'
receiver = '2254078@qq.com'
subject = '回家收拾行李通知,测试邮件发送 python,来自LHH-James的问候'
smtpserver = 'smtp.163.com'
username = '13799403094@163.com'
password = '87763145'  # 是授权密码，而不是登录密码
#
# msg = MIMEText('晚上8点开会,请务必到达参加！！！内容在哪里 ，为什么没看见  没看见   没看见。。。。。。，没看见没看见。。。。。', 'plain', 'utf-8')  # 中文需参数‘utf-8’，单字节字符不需要
msg = MIMEText('晚上记得收拾好东西,明天回家东西别漏了哈！python  测试邮件发送,看到没有，看到没有，看到记得回复哈。。。。。。 看到记得回复哈. 看到记得回复哈!!!!','plain', 'utf-8')  # 中文需参数‘utf-8’，单字节字符不需要

msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'James<13799403094@163.com>'
msg['To'] = '尤克里里<2254078@qq.com>'

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

