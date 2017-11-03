import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','smscontacts.settings')


import django
django.setup()

from smscontacts.models import TemplateText

def populate():

    python_TemplateText = [
      {
        "template_name": "Fondation Beyeler Starkregen Warnung",
        "template_text": "Manuelle Wetterwarnung: Starkregen (Mehr als 80 mm) innerhalb der nächsten 24 Stunden zu erwarten"
      },
      {
        "template_name": "Fondation Beyeler Wind Warnung",
        "template_text": "Manuelle Wetterwarnung Wind Riehen: Vorhersage: XXX Bft in den nächsten 6 Stunden Bei Fragen und Unsicherheiten kontaktieren sie unseren Prognostiker: 0900 57 61 52 (3.13/Min ab Festnetz)"
      },
      {
        "template_name": "TBA Bern Niederschlag Warnung",
        "template_text": "Wetterwarnung: Regen in weniger als 20 km Entfernung (Bern)"
      },
      {
        "template_name": "TBA Bern Niederschlag Alarm",
        "template_text": "Wetteralarm: Regen in weniger als 10 km Entfernung (Bern)"
      },
      {
        "template_name": "Sulgenbachkanal Niederschlag Warnung",
        "template_text": "Wetterwarnung: Regen in weniger als 20 km Entfernung (Bern)"
      },
      {
        "template_name": "Sulgenbachkanal Niederschlag Alarm",
        "template_text": "Wetteralarm: Regen in weniger als 10 km Entfernung (Bern)"
      },
      {
        "template_name": "Zieglerstrasse Niederschlag Erheblich",
        "template_text": "Wetteralarm Zieglerstrasse: Erheblicher Regen (Stufe 3) in weniger als 20 km Entfernung (Bern)"
      },
      {
        "template_name": "Zieglerstrasse Niederschlag Grosse Gefahr",
        "template_text": "Wetteralarm Zieglerstrasse: Grosse Gefahr (Stufe 4) Regen in weniger als 10 km Entfernung (Bern)"
      },
      {
        "template_name": "Jungfrau Gewitter Warnung",
        "template_text": "Jungfraujoch Wetterhinweis Stufe 1: Hohes Gewitterpotential innerhalb der nächsten Stunde vorhanden"
      },
      {
        "template_name": "Jungfrau Gewitter Alarm",
        "template_text": "Jungfraujoch Wetterhinweis Stufe 2: Akutes Gewitterpotential. Gewitter in den folgenden Minuten wahrscheinlich"
      },
      {
        "template_name": "Jungfrau Wind Warnung",
        "template_text": "Jungfraujoch Wetterhinweis Stufe 1: Windspitze über 75km/h erwartet in den folgenden 3 Stunden"
      },
      {
        "template_name": "Jungfrau Wind Alarm",
        "template_text": "Jungfraujoch Wetterhinweis Stufe 2: Windspitzen aktuell über 75km/h"
      },
      {
        "template_name": "Sagi Openair Gewitter",
        "template_text": "Sagi Openair Wetterhinweis: Gewitter in den nächsten 60 Minuten erwartet"
      },
      {
        "template_name": "Sagi Openair Wind",
        "template_text": "Sagi Openair Wetterhinweis: Wind über 70 km/h in den nächsten 60 Minuten erwartet"
      },
      {
        "template_name": "OHA Thun Wind Alarm",
        "template_text": "OHA Thun Wetterhinweis Wind: Sturm über 80 km/h erwartet"
      },
      {
        "template_name": "OHA Thun Regen Alarm",
        "template_text": "OHA Thun Wetterhinweis: Starker Niederschlag in den nächsten 30 Minuten erwartet"
      },
      {
        "template_name": "Test",
        "template_text": "Dies ist eine Testnachricht der Wetterüberwachung. Bitte überprüfen Sie dass alle Zuständigen diese Nachricht erhalten haben. Beste Grüsse, Ihr Meteotest-Team."
      }
    ]
    print(python_TemplateText)

    cats = {"Populate": {"template_data": python_TemplateText}}

# If you want to add more catergories or pages,
    l = len(python_TemplateText)
    print(l)

    for  cat, cat_data in cats.items():
      for n in range(0,l - 1):
        print(cat_data["template_data"][n]["template_name"], "\n",  cat_data["template_data"][n]["template_text"])
        tname  = cat_data["template_data"][n]["template_name"]
        ttext =  cat_data["template_data"][n]["template_text"]
        TemplateText.objects.get_or_create(template_name=tname,template_text=ttext)


populate()
