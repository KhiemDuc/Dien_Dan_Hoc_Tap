# Generated by Django 3.2.7 on 2022-11-24 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_user_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='@', max_length=200),
        ),
    ]
