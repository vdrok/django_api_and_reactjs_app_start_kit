# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-16 11:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Talent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='Male', max_length=10)),
                ('phone_number', models.CharField(blank=True, max_length=30)),
                ('mailing_addresse1', models.CharField(blank=True, max_length=100)),
                ('mailing_addresse2', models.CharField(blank=True, max_length=100)),
                ('mailing_addresse3', models.CharField(blank=True, max_length=100)),
                ('mailing_addresse4', models.CharField(blank=True, max_length=100)),
                ('birthday', models.DateTimeField()),
                ('emergency_first_name', models.CharField(blank=True, max_length=50)),
                ('emergency_last_name', models.CharField(blank=True, max_length=50)),
                ('emergency_email', models.CharField(blank=True, max_length=100)),
                ('emergency_phone', models.CharField(blank=True, max_length=30)),
                ('emergency_relationship', models.CharField(blank=True, max_length=100)),
                ('passport_expiration_data', models.DateTimeField(blank=True)),
                ('passport_number', models.CharField(blank=True, max_length=100)),
                ('expiration_date', models.DateTimeField(blank=True)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('bmi', models.FloatField()),
                ('age_range', models.CharField(blank=True, default='', max_length=100)),
                ('head_line', models.CharField(blank=True, max_length=100)),
                ('bio', models.TextField()),
                ('worked_cruise_ship', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talent', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'talent',
                'ordering': ('id',),
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='talent',
            unique_together=set([('user', 'id')]),
        ),
    ]
