# Generated by Django 3.0.7 on 2020-06-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='result',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
