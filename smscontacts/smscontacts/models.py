from django.db import models

class TemplateText(models.Model):

    template_name = models.CharField(max_length=128, unique=True)
    template_text = models.TextField()

    class Meta:
        verbose_name_plural = 'Templates'

    def __str__(self): #
        return self.template_name

class Contact(models.Model):

    contact_name = models.CharField(max_length=128, unique=True)
    contact_numbers = models.CharField(max_length=128)

    def __str__(self): #
        return self.contact_name

class Group(models.Model):

    group_name = models.CharField(max_length=128, unique=True)
    contacts = models.ManyToManyField(Contact)

    def __str__(self): #
        return self.group_name




