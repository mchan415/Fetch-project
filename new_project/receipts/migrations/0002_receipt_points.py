# Generated by Django 5.1.6 on 2025-03-06 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
