# this code must use environment variables for original config as we will be changing the application config

import os
from src import config
from flask_mail import Mail
from flask import current_app
from flask_mail import Message
from src.exceptions import ApplicationError
# from src.sql import Sql


def get_smtp_config(email):
	mail = Mail()
	# results = Sql.get_email_account_for_company(company_name)
	# print(results)
	# if len(results) == 1:
	# 	email_account = results[0]
	# 	config.update(dict(
	# 		MAIL_SERVER = email_account.server,
	# 		MAIL_PORT = email_account.port,
	# 		MAIL_USE_TLS = email_account.tls,
	# 		MAIL_USE_SSL = email_account.ssl,
	# 		MAIL_USERNAME = email_account.username,
	# 		MAIL_PASSWORD = email_account.password,
	# 	))
	# else:
	config.update(dict(
		MAIL_SERVER = os.environ['MAIL_SERVER'],
		MAIL_PORT = os.environ['MAIL_PORT'],
		MAIL_USE_TLS = False,
		MAIL_USE_SSL = False,
		MAIL_USERNAME = email
		# MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
	))


	mail.init_app(app)
	return mail

def send_mail(title, recipient, body, html_content):
	mail = get_smtp_config('')
	msg = Message(
            title,
            sender=app.config['MAIL_USERNAME'],
            recipients=recipient
            )

	msg.html = html_content

	try:
		mail.send(msg)
	except Exception as e:
		print(e)
		current_app.logger.error('Unhandled Exception: %s', repr(e))
		raise ApplicationError('something has gone sending email', 'unspecified')
	else:
		current_app.logger.info('email sent')
		return "sent"
