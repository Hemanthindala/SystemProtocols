# Generated by Django 4.2.10 on 2024-02-12 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalservices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('Price', models.IntegerField()),
                ('Rooms', models.IntegerField()),
                ('Bath', models.IntegerField()),
            ],
        ),
    ]
