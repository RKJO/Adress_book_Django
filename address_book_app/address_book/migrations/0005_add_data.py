# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations
from address_book.models import Person, Address, Phone, Email


def add_data(apps, schema_editor):
    p1 = Person.objects.get(id=31)
    p2 = Person.objects.get(id=32)
    p3 = Person.objects.get(id=33)
    p4 = Person.objects.get(id=34)
    p5 = Person.objects.get(id=35)
    p6 = Person.objects.get(id=36)
    Address.objects.create(city="Warszawa", street="Przyokopowa",  building_num="33", person=p3)
    Address.objects.create(city="Szczecin", street="Nadmorska",  building_num="77", flat_num="136", person=p2)
    Address.objects.create(city="Gdańsk", street="Oksywje",  building_num="44", flat_num="100", person=p6)
    Phone.objects.create(phone_number=555833495, type="Domowy", person=p6)
    Phone.objects.create(phone_number=209102343, type="Prywatny", person=p5)
    Phone.objects.create(phone_number=655699120, type="Praca", person=p6)
    Phone.objects.create(phone_number=372737729, type="Praca", person=p2)
    Phone.objects.create(phone_number=655651071, type="Domowy", person=p1)
    Phone.objects.create(phone_number=209126258, type="Firmowy", person=p5)
    Email.objects.create(email_address="roman.warkocz@gmail.com", type="Prywatny", person=p1)
    Email.objects.create(email_address="anka.cikoretka@buziaczek.pl", type="Prywatny", person=p3)
    Email.objects.create(email_address="h.kania@praca.pl", type="Firmowy", person=p4)
    Email.objects.create(email_address="john.motyka@robota.com", type="Firmowy", person=p6)


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0004_auto_20180629_1029'),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]