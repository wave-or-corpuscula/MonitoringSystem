# Generated by Django 4.1.5 on 2023-08-19 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0003_alter_prices_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
