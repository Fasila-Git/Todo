# Generated by Django 4.2.3 on 2023-07-28 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='taskDate',
            field=models.DateField(default='2002-07-27'),
            preserve_default=False,
        ),
    ]