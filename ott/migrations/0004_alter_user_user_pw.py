# Generated by Django 3.2.7 on 2021-09-27 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ott', '0003_alter_user_user_pw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_pw',
            field=models.TextField(max_length=100),
        ),
    ]