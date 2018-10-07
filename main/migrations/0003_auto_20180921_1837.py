# Generated by Django 2.1.1 on 2018-09-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180921_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='options',
        ),
        migrations.RemoveField(
            model_name='options',
            name='type',
        ),
        migrations.AddField(
            model_name='categories',
            name='optiontype',
            field=models.ManyToManyField(to='main.OptionType'),
        ),
        migrations.AddField(
            model_name='optiontype',
            name='options',
            field=models.ManyToManyField(to='main.Options'),
        ),
    ]