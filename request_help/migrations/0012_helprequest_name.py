# Generated by Django 3.0.3 on 2020-04-27 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_help', '0011_auto_20200413_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='helprequest',
            name='name',
            field=models.CharField(default='Not Real Name', max_length=60),
        ),
    ]
