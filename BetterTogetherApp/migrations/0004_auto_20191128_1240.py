# Generated by Django 2.2.5 on 2019-11-28 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BetterTogetherApp', '0003_auto_20191128_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='phone_num',
            field=models.CharField(default=0, max_length=10, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='shareride',
            name='date_time',
            field=models.DateTimeField(default='2019-11-28 12:40:41', verbose_name='Date and Time'),
        ),
    ]
