import smtplib
from email.mime.text import MIMEText

send_email = "chc853@naver.com"
send_pwd = "0000000"
recv_email = "chc853@gmail.com"

smtp_name = "smtp.naver.com"
smtp_port = 587

text = """
메일의 내용을 여기에 적습니다.
여러줄을 넣어도 됩니다.
"""

msg = MIMEText(text)
msg['Subject'] = "python mail text"
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s=smtplib.SMTP(smtp_name,smtp_port)
s.starttls()
s.login(send_email,send_pwd)
s.sendmail(send_email,recv_email,msg.as_string())
s.quit()


