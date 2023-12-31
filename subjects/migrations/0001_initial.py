# Generated by Django 4.2.6 on 2023-11-22 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectNo', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('label', models.CharField(max_length=30, null=True)),
                ('createdAt', models.DateField(default=datetime.date.today, max_length=30)),
                ('updatedAt', models.DateField(default=datetime.date.today, max_length=30)),
            ],
        ),
    ]
