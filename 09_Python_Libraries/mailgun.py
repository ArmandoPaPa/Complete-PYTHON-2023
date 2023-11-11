import requests

MAILGUN_API_URL = '___'
MAILGUN_API_KEY = '___'

FROM_NAME = 'Armando'
FROM_EMAIL = 'sender@mail.com'

TO_EMAILS = ['another@gmail.com', 'yet_another@gmail.com']

SUBJECT = 'Test e-mail'
CONTENT = 'Hello, this is a test e-mail'

requests.post(
    MAILGUN_API_URL,
    auth=('api', MAILGUN_API_KEY),
    data={
        'from': f'{FROM_NAME} <{FROM_EMAIL}>',
        'to': TO_EMAILS,
        'subject': SUBJECT,
        'text': CONTENT
    }
)