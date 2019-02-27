'''
hello_email.py
--------------

This file is the "Hello, World!" for the sendgrid API, with a
couple modifications. It requires an api key and e-mail address
to be environment e-mails.

This file sends a simple email and prints the response.
'''

import os
import sendgrid
from sendgrid.helpers.mail import Email, Content, Mail

sg_api_key = os.environ.get('SENDGRID_API_KEY')
test_email = os.environ.get('TEST_EMAIL')

sg = sendgrid.SendGridAPIClient(apikey=sg_api_key)

from_email = Email(test_email)
to_email = Email(test_email)
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")

mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())

print(response.status_code)
print(response.body)
print(response.headers)
