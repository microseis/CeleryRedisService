# -*- coding: utf-8 -*-
from mailer.celerysettings import app
import os
from .models import Contact

from dotenv import load_dotenv
from django.template.loader import get_template
import uuid
from django.core.mail import EmailMultiAlternatives
import time


load_dotenv()


@app.task
def send_bulk_email(data):
    time.sleep(30)
    for user in Contact.objects.all():
        user.unique_code = uuid.uuid4()
        user.save()
        template = get_template("main/mail_template.html")
        context_data = dict()
        context_data["image_url"] = data
        context_data['user'] = user.firstname
        url_is = context_data["image_url"] + "/" + str(user.unique_code) + "/"
        context_data['url_is'] = url_is
        html_text = template.render(context_data)
        email = user.email
        subject, from_email, to = u"Отложенное сообщение от разработчика", os.environ.get('SENDER_EMAIL'), [user.email]

        msg = EmailMultiAlternatives(subject, html_text, from_email, to)
        msg.attach_alternative(html_text, "text/html")
        msg.content_subtype = 'html'
        msg.send()

