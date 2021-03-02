from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template


def send_email(subject=None, message=None, recipient_list=None):
    email_from = settings.EMAIL_HOST_USER
    email_template = get_template('send_email_template.html')
    send_mail(subject, message, email_from, recipient_list,
              html_message=email_template.render())


def sing_up_email(recipient_list=None, activate_user_url=None):
    subject = 'Спасибо за регистрацию!'
    message = f'Добро пожаловать! Для активации ' \
              f'вашего аккаунта перейдите по ссылке:\n' \
              f'{activate_user_url}'
    email_from = settings.EMAIL_HOST_USER
    email_template = get_template('sing_up_email_template.html')
    send_mail(subject, message, email_from, recipient_list,
              html_message=email_template.render(context={
                  'activate_user_url': activate_user_url
              }))
