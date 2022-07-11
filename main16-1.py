import imaplib
import email
from email import policy
import requests
import json

slack_webhook_url = "https://hooks.slack.com/services/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"

def sendSlackWebhook(strText):
    headers = {
        "Content-type":"application/json"
    }
    
    data = {
        "text" : strText
    }
    
    res = requests.post(slack_webhook_url,headers=headers,data=json.dumps(data))
    
    if res.status_code == 200:
        return "ok"
    else:
        return "error"

def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = 'chc853'
pw = '!#zaq1xsw2'
imap.login(id,pw)

imap.select('INBOX')
resp, data = imap.uid('search',None,'All')
all_email = data[0].split()
#print('*'*70)
#print(all_email)
last_email = all_email[-5:]

for mail in reversed(last_email):
    result, data = imap.uid('fetch',mail,'(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email,policy=policy.default)
    print('='*70)
    print('FROM: ',email_message['From'])
    print('SENDER: ',email_message['Sender'])
    print('TO: ',email_message['To'])
    print('DATE: ',email_message['Date'])
    subject, encode = find_encoding_info(email_message['Subject'])
    print('SUBJECT: ',subject)
    print('='*70)
    
    #print('[CONTENT]')
    message = ' '
    if email_message.is_multipart():
        for part in email_message.get_payload():
            if part.get_content_type() == 'text/plain':
                bytes = part.get_payload(decode=True)
                encode = part.get_content_charset()
                message = message + str(bytes,encode)
    
    #print(message)
    #print('='*70)            
    
    emain_from = str(email_message['From'])
    emain_date = str(email_message['Date'])
    subject_str = str(subject)
    if subject_str.find("예스") >=0:
        slack_send_message = emain_from+ '\n' + emain_date+ '\n' +subject_str
        sendSlackWebhook(slack_send_message)
        print(slack_send_message)
    
imap.close()
imap.logout()