# Generated by Django 3.1.2 on 2020-10-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsinorder',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]