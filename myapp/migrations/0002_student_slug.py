# Generated by Django 4.0.6 on 2022-08-04 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]