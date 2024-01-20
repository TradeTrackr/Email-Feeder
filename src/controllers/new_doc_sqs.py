from email.message import Message
import smtplib
from flask import render_template
from src.dependencies.smtp_config import send_mail

from src import config


class NewDocSqs(object):
    def __init__(self, body):
        print("doing some stuff", flush=True)
        send_email_initial(body)

        print("ok finished now", flush=True)


def send_email_initial(body):


    base_domain = config.BASE_DOMAIN
    # Define these once; use them twice!
    strFrom = body['from_email']
    strTo = body['email']

    html_content = render_template('../tempates/pages/enquiry_email.html', body=body)
    return send_mail(
        body['email_title'],
        strFrom,
        [strTo],
        html_content
        )

