# Generated by Django 3.2.3 on 2021-06-22 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='portfolio/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
