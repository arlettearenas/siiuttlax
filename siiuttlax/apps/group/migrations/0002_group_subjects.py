# Generated by Django 5.0.6 on 2024-08-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0001_initial'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='subjects',
            field=models.ManyToManyField(to='careers.subject'),
        ),
    ]