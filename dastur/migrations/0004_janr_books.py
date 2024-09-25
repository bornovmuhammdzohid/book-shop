# Generated by Django 5.0.6 on 2024-09-23 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dastur', '0003_category_maxsulot_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Janr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('janrlar', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('ovner', models.CharField(max_length=100)),
                ('narx', models.IntegerField()),
                ('janr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dastur.janr')),
            ],
        ),
    ]
