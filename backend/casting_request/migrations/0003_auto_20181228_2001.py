# Generated by Django 2.0.5 on 2018-12-28 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casting_request', '0002_castingrequest_status_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='castingrequest',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Requested', 'Requested'), ('Reviewing', 'Reviewing'), ('In Progress', 'In Progress'), ('Accepted', 'Accepted'), ('Declined', 'Declined'), ('Canceled', 'Canceled'), ('Completed', 'Completed')], default='Draft', max_length=10),
        ),
    ]
