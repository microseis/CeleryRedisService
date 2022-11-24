# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import CreateView
from rest_framework.generics import get_object_or_404
from .models import Contact
from .forms import ContactForm
from .tasks import send_bulk_email
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
import os
from django.template.loader import get_template

from PIL import Image
from rest_framework import status
from .serializer import GetDataSerializer
from dotenv import load_dotenv

load_dotenv()


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = 'send/subscribed'
    template_name = 'main/contact.html'

    def form_valid(self, form):
        form.save()
        return super(ContactView, self).form_valid(form)


class SendTemplateMailView(APIView):

    def post(self, request, *args, **kwargs):
        for user in Contact.objects.all():
            user.unique_code = uuid.uuid4()
            user.save()
            template = get_template("main/mail_template.html")
            context_data = dict()
            context_data["image_url"] = request.build_absolute_uri("image_load")
            context_data['user'] = user.firstname
            url_is = context_data["image_url"] + "/" + str(user.unique_code) + "/"
            context_data['url_is'] = url_is
            html_text = template.render(context_data)
            email = user.email
            subject, from_email, to = u"Сообщение от разработчика", os.environ.get('SENDER_EMAIL'), [user.email]

            msg = EmailMultiAlternatives(subject, html_text, from_email, to)
            msg.attach_alternative(html_text, "text/html")
            msg.content_subtype = 'html'
            msg.send()
        return HttpResponse("Emails were sent!")


class GetDataView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(Contact.objects.all(), pk=pk)
        serializer = GetDataSerializer(user)
        return Response({"Data": serializer.data})


class ImageView(APIView):

    def get(self, request, slug):
        red = Image.new('RGB', (20, 20), color='white')
        response = HttpResponse(content_type="image/png", status=status.HTTP_200_OK)
        user = Contact.objects.get(unique_code=slug)
        user.counter_is = "mail opened"
        user.save()
        red.save(response, "PNG")
        return Response({"Image view": "success"})


def subscribed(request):
    return HttpResponse("Thank you for the subscription! ")


def sendbulk(request):
    if request.method == "POST":
        data = request.build_absolute_uri("image_load")
        send_bulk_email.apply_async(args=[data], countdown=10, expires=15)
        return HttpResponse("Emails will be sent in 1 minute")
