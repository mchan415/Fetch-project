# Generated by Django 5.1.6 on 2025-03-05 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='points',
        ),
    ]
