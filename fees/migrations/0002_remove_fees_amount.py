# Generated by Django 4.2.6 on 2023-11-16 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fees',
            name='amount',
        ),
    ]
