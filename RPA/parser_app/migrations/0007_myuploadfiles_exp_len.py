# Generated by Django 3.2.11 on 2022-03-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0006_myuploadfiles_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuploadfiles',
            name='exp_len',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name'),
        ),
    ]
