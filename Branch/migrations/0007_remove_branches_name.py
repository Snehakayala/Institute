# Generated by Django 3.1.7 on 2021-04-07 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0006_branches_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branches',
            name='name',
        ),
    ]
