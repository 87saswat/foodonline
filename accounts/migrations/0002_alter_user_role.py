# Generated by Django 4.1.1 on 2022-09-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Restaurant'), (2, 'Customer')], null=True),
        ),
    ]
