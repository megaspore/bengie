# Generated by Django 4.1.1 on 2022-10-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsons',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
