# Generated by Django 4.2.6 on 2023-11-16 16:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentNo', models.CharField(max_length=20, unique=True)),
                ('firstname', models.CharField(max_length=15, null=True)),
                ('middlename', models.CharField(max_length=15, null=True)),
                ('lastname', models.CharField(max_length=15, null=True)),
                ('dob', models.DateField(max_length=30, null=True)),
                ('address', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(max_length=5, null=True)),
                ('nationality', models.CharField(default='Ghanaian', max_length=15, null=True)),
                ('religion', models.CharField(max_length=15, null=True)),
                ('previousSchoolAttended', models.CharField(max_length=20, null=True)),
                ('previousSchoolClass', models.CharField(max_length=10, null=True)),
                ('disability', models.CharField(max_length=20, null=True)),
                ('createdAt', models.DateField(default=datetime.date.today, max_length=30)),
                ('updatedAt', models.DateField(default=datetime.date.today, max_length=30)),
                ('parentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parents.parents')),
            ],
        ),
    ]