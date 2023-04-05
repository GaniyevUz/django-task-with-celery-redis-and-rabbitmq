from celery import shared_task
from django.core.mail import EmailMessage

from root.settings import EMAIL_HOST_USER


@shared_task
def send_to_gmail(email):
    print('ACCEPT TASK')

    subject = 'test subject'
    message = "Hello, {email}! <br> This is test message."

    recipient_list = [email]

    email = EmailMessage(subject, message, EMAIL_HOST_USER, recipient_list)
    email.content_subtype = 'html'
    result = email.send()
    print('Send to MAIL')
    return result
