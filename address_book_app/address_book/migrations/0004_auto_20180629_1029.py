# Generated by Django 2.0.6 on 2018-06-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0003_add_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
