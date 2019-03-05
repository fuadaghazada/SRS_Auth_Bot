#!/usr/bin/python
import re
import time
from mechanize import Browser

import config

br = Browser()

# Ignore robots.txt
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]

br.open( "https://stars.bilkent.edu.tr/srs" )

# Selecting the login form in the site
br.select_form(class_='form-horizontal')

# ID
control = br.form.controls[0]
control.readonly = False
br[control.name] = config.ID

# Password
control = br.form.controls[1]
control.readonly = False
br[control.name] = config.PASS

# Hidden password :P
control = br.form.controls[2]
control.readonly = False
br[control.name] = config.PASS

# Submit
response = br.submit();

# Confirmation Page
br.select_form(class_='form-horizontal')

time.sleep(2)
import auth_mail
verf_code = auth_mail.code

if verf_code is not None:
    control = br.form.controls[0]
    control.readonly = False
    br[control.name] = str(verf_code)

    print(control.value)

    # Submit verification
    response = br.submit();

    print(response.read())

else:
    print("Something went wrong!")
