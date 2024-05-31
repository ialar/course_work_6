import smtplib
from datetime import datetime, timedelta
import pytz
# from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from main.models import Mailing, Logs


def mailing_job():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    day = timedelta(days=1, hours=0, minutes=0)
    weak = timedelta(days=7, hours=0, minutes=0)
    month = timedelta(days=30, hours=0, minutes=0)

    mailings = (
        Mailing.objects.all()
        .filter(status="created")
        .filter(is_active=True)
        .filter(next_date__lte=current_datetime)
        .filter(end_date__gte=current_datetime)
    )
    print(mailings)

    for mail in mailings:
        response = 'Исключения не генерировались'
        mail.status = 'launched'
        mail.save()
        emails_list = [client.email for client in mail.client.all()]
        try:
            result = send_mail(subject=mail.message.theme,
                               message=mail.message.text,
                               from_email=settings.EMAIL_HOST_USER,
                               recipient_list=emails_list,
                               fail_silently=False)
            print('RESULT', result)
        except smtplib.SMTPException as e:
            response = e

        if result == 1:
            status = 'Отправлено'
            print('Отправлено')
        else:
            status = 'Ошибка отправки'
            print('Ошибка отправки')

        last_mailing_time = Logs.last_mailing_time
        log = Logs(mailing=mail, status=status, response=response, last_mailing_time=last_mailing_time)
        log.save()
        print(log)

        if mail.periodicity == 'day':
            mail.next_date = log.last_mailing_time + day
        elif mail.periodicity == 'week':
            mail.next_date = log.last_mailing_time + weak
        elif mail.periodicity == 'month':
            mail.next_date = log.last_mailing_time + month

        if mail.next_date < mail.end_date:
            mail.status = 'created'
        else:
            mail.status = 'finished'
        mail.save()
