# Generated by Django 3.2.11 on 2022-03-11 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0009_auto_20220311_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuploadfiles',
            name='experience',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Experience'),
        ),
    ]
