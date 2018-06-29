# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations
from address_book.models import Person, Address, Phone, Email, Group


def add_data(apps, schema_editor):
    Person.objects.create(first_name="Roman", last_name="Warkocz", description="Pan Roman erotoman")
    Person.objects.create(first_name="Izzy", last_name="Boo", description="Moja Ona")
    Person.objects.create(first_name="Ania", last_name="Sikora", description="Uwaga!!!")
    Person.objects.create(first_name="Henryk", last_name="Kania", description="Jego lubi Ania")
    Person.objects.create(first_name="Luk", last_name="Goof")
    Person.objects.create(first_name="Janek", last_name="Motyka")
    # Address.objects.create(city="Warszawa", street="Przyokopowa",  building_num="33")
    # Address.objects.create(city="Szczecin", street="Nadmorska",  building_num="77", flat_num="136")
    # Address.objects.create(city="Gdańsk", street="Oksywje",  building_num="44", flat_num="100")
    # Phone.objects.create(phone_number=555833495, type="Domowy")
    # Phone.objects.create(phone_number=209102343, type="Prywatny")
    # Phone.objects.create(phone_number=655699120, type="Praca")
    # Phone.objects.create(phone_number=372737729, type="Praca")
    # Phone.objects.create(phone_number=655651071, type="Domowy")
    # Phone.objects.create(phone_number=209126258, type="Firmowy")
    # Email.objects.create(email_address="roman.warkocz@gmail.com", type="Prywatny")
    # Email.objects.create(email_address="anka.cikoretka@buziaczek.pl", type="Prywatny")
    # Email.objects.create(email_address="h.kania@praca.pl", type="Firmowy")
    # Email.objects.create(email_address="john.motyka@robota.com", type="Firmowy")
    Group.objects.create(name="Domownicy")
    Group.objects.create(name="Praca")
    Group.objects.create(name="Kumple")
    Group.objects.create(name="Grupa W")


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0002_auto_20180629_0943'),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]