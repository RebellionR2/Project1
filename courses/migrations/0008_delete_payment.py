# Generated by Django 4.2.1 on 2023-06-19 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_usercourse_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
