# Generated by Django 4.1.7 on 2023-03-31 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('mobileno', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
