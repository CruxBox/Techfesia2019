# Generated by Django 2.2.2 on 2019-06-16 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_firebaseuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
