# Generated by Django 4.2.10 on 2024-02-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('Seats', models.IntegerField()),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
