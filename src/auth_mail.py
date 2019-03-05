import poplib
import re

import config

code = None

connection = poplib.POP3_SSL(config.HOST)

# Setting email and password for mail
connection.user(config.MAIL)
connection.pass_(config.MAIL_PASS)

## get information about the email address
count, con_stat = connection.stat()
last_email = connection.retr(count)

cnt_size = len(last_email[1])
verf_text = str(last_email[1][cnt_size - 2])
code = re.search(r'\d+', verf_text, re.M|re.I)
if(code):
    code = code.group()
