# Generated by Django 3.2.5 on 2021-09-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ott', '0002_user_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_pw',
            field=models.CharField(max_length=100),
        ),
    ]
