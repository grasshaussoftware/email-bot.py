import re
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


fp = open('message.txt', 'rb')
msg = MIMEText(fp.read())
fp.close()
msg['Subject'] = 'subject'
msg['From'] = 'account@email.com'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('account@gmail.com', 'password')
email_data = csv.reader(open('contacts.csv', 'rb'))
email_pattern= re.compile("^.+@.+\..+$")
for row in email_data:
  if( email_pattern.search(row[0]) ):
    del msg['To']
    msg['To'] = row[0]
    try:
      server.sendmail('test@gmail.com', [row[0]], msg.as_string())
    except SMTPException:
      print ("An error occured.")
server.quit()
