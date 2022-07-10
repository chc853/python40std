from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText

send_email = "chc853@naver.com"
send_pwd = "000000"
recv_email = "chc853@gmail.com"

smtp_name = "smtp.naver.com"
smtp_port = 587

msg = MIMEMultipart()

html_body = """
<!-- #######  THIS IS A COMMENT - Visible only in the source editor #########-->
<h2>Welcome To The Best Online HTML Web Editor!</h2>
<p style="font-size: 1.5em;">You can <strong style="background-color: #317399; padding: 0 5px; color: #fff;">type your text</strong> directly in the editor or paste it from a Word Doc, PDF, Excel etc.</p>
<p style="font-size: 1.5em;">The <strong>visual editor</strong> on the right and the <strong>source editor</strong> on the left are linked together and the changes are reflected in the other one as you type! <img src="https://html5-editor.net/images/smiley.png" alt="smiley" /></p>
<table class="editorDemoTable">
<tbody>
<tr>
<td><strong>Name</strong></td>
<td><strong>City</strong></td>
<td><strong>Age</strong></td>
</tr>
<tr>
<td>John</td>
<td>Chicago</td>
<td>23</td>
</tr>
<tr>
<td>Lucy</td>
<td>Wisconsin</td>
<td>19</td>
</tr>
<tr>
<td>Amanda</td>
<td>Madison</td>
<td>22</td>
</tr>
</tbody>
</table>
<p>This is a table you can experiment with.</p>
"""

msg['Subject'] = "python mail for html"
msg['From'] = send_email
msg['To'] = recv_email

msg.attach(MIMEText(html_body,'html'))
#print(msg.as_string())

s=smtplib.SMTP(smtp_name,smtp_port)
s.starttls()
s.login(send_email,send_pwd)
s.sendmail(send_email,recv_email,msg.as_string())
s.quit()


