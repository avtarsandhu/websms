
from smscontacts.models import TemplateText
from smscontacts.models import Group
from smscontacts.models import Contact



from rest_framework import serializers


class SmsTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateText
        fields = ('template_name', 'template_text')



class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('contact_name', 'contact_numbers')


class GroupSerializer(serializers.ModelSerializer):

    contacts = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('group_name', 'contacts')
