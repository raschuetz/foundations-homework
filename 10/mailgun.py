import requests
import time
datestring = time.strftime('%B %-m, %Y')
datestring_att = time.strftime('%Y-%m-%d')
filename = 'reddit-data-' + datestring_att + '.csv'
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox4ddf46fe35524707ad8912c724e1d928.mailgun.org/messages",
        auth=("api", "key-2b57751d83581145c41c4f53b2d32ce7"),
        files=[("attachment", open(filename))],
        data={"from": "Mailgun Sandbox <postmaster@sandbox4ddf46fe35524707ad8912c724e1d928.mailgun.org>",
              "to": "Rebecca Schuetz <rebecca.a.schuetz@gmail.com>",
              "subject": "Reddit This Morning: " + datestring,
              "text": 'This is where the CSV goes'})

send_simple_message()
