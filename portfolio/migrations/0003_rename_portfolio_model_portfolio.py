# Generated by Django 3.2.3 on 2021-06-22 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_rename_portfolio_portfolio_model'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='portfolio_model',
            new_name='portfolio',
        ),
    ]
