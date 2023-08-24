# Generated by Django 4.1.5 on 2023-08-24 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parsing.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Observed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('good_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parsing.goods')),
                ('observed_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parsing.observed')),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField()),
                ('good_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parsing.goods')),
                ('observed_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parsing.observed')),
            ],
        ),
    ]
