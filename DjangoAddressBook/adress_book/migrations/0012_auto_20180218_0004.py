# Generated by Django 2.0.1 on 2018-02-17 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adress_book', '0011_auto_20180217_2342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactinfo',
            old_name='user_id',
            new_name='user_name',
        ),
    ]
