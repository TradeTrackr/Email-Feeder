
from src.dependencies.emails import EmailAPI


class NewDocSqs(object):
    def __init__(self, body):
        print("doing some stuff", flush=True)
        send_email_initial(body)

        print("ok finished now", flush=True)

def send_email_initial(body):
    EmailAPI().new_email(body)
