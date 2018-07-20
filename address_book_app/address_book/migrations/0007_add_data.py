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
    p1.address = Address.objects.get(id=8)
    p2.address = Address.objects.get(id=6)
    p3.address = Address.objects.get(id=7)
    p4.address = Address.objects.get(id=7)
    p5.address = Address.objects.get(id=6)
    p6.address = Address.objects.get(id=8)


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0006_auto_20180629_1325'),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]