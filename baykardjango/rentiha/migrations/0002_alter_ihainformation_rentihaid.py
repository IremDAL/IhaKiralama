# Generated by Django 5.0.1 on 2024-01-25 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentiha', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ihainformation',
            name='rentihaid',
            field=models.ForeignKey(limit_choices_to={'isDeleted': False, 'rentalActive': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rentiha.ihaalls'),
        ),
    ]
