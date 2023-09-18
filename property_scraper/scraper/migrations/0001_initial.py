# Generated by Django 4.2.5 on 2023-09-18 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=255)),
                ('property_cost', models.CharField(max_length=255)),
                ('property_area', models.CharField(max_length=255)),
                ('property_type', models.CharField(max_length=255)),
                ('property_locality', models.CharField(max_length=255)),
                ('property_link', models.CharField(max_length=255)),
            ],
        ),
    ]