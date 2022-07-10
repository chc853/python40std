from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from fileinput import filename
import smtplib
from email.mime.text import MIMEText

send_email = "chc853@gmail.com"
send_pwd = "lxqtuqszldwkjmbj"
recv_email = "chc853@naver.com"

smtp_name = "smtp.gmail.com"
smtp_port = 587

msg = MIMEMultipart()


text = """
메일의 내용을 여기에 적습니다.
여러줄을 넣어도 됩니다.
"""
msg['Subject'] = "python mail text"
msg['From'] = send_email
msg['To'] = recv_email

contentPart = MIMEText(text)
msg.attach(contentPart)

etc_file_path = r'.\성춘향.pdf'
with open(etc_file_path, 'rb') as f:
    etc_part = MIMEApplication(f.read())
    etc_part.add_header('Content-Disposition','attachment',filename="성춘향.pdf")
    msg.attach(etc_part)

#print(msg.as_string())

s=smtplib.SMTP(smtp_name,smtp_port)
s.starttls()
s.login(send_email,send_pwd)
s.sendmail(send_email,recv_email,msg.as_string())
s.quit()


