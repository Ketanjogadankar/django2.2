# Generated by Django 3.0.4 on 2020-03-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20200329_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phonnum',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
    ]
