# Generated by Django 5.1.3 on 2024-12-03 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opportunity',
            name='date_created',
        ),
    ]