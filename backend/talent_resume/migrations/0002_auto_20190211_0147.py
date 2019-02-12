# Generated by Django 2.0.5 on 2019-02-11 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent_resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talentresume',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='talentresume',
            name='approved_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]