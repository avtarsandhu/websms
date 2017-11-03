from django.contrib import admin

from smscontacts.models import TemplateText , Contact , Group


admin.site.register(TemplateText)
admin.site.register(Contact)
admin.site.register(Group)


