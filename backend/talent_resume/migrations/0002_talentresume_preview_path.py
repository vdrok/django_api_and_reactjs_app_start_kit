# Generated by Django 2.0.2 on 2018-08-13 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent_resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talentresume',
            name='preview_path',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]