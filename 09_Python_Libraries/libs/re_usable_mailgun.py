import requests

class Mailgun:

    MAILGUN_API_URL = '___'
    MAILGUN_API_KEY = '___'

    FROM_NAME = 'Armando'
    FROM_EMAIL = 'sender@mail.com'

    @classmethod
    def send_email(cls, to_emails, subject, content, from_name=FROM_NAME, from_email=FROM_EMAIL):
        requests.post(
            cls.MAILGUN_API_URL,
            auth=('api', cls.MAILGUN_API_KEY),
            data={
                'from': f'{from_name} <{from_email}>',
                'to': to_emails,
                'subject': subject,
                'text': content
            }
        )
