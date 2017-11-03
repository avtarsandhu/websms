from django.shortcuts import render

# Create your views here.
from smscontacts.models import TemplateText
from smscontacts.models import Group
from smscontacts.models import Contact

from sms_templates_app.serializers import SmsTextSerializer
from sms_templates_app.serializers import GroupSerializer
from sms_templates_app.serializers import ContactSerializer


from django.db.models import prefetch_related_objects

from rest_framework.views import APIView
from rest_framework.response import Response


class TemplateList(APIView):
    def get(self, request, format=None):
        templatetext = TemplateText.objects.all()
        serializer = SmsTextSerializer(templatetext , many=True)
        return Response(serializer.data)


class ContactList(APIView):
    def get(self, request, format=None):
        contactlist = Contact.objects.all()
        serializer = ContactSerializer(contactlist , many=True)
        return Response(serializer.data)


class GroupList(APIView):
    def get(self, request, format=None):
        groupcontacts = Group.objects.all()
        groupcontacts = groupcontacts.prefetch_related('contacts')

        serializer = GroupSerializer(groupcontacts , many=True)
        return Response(serializer.data)

