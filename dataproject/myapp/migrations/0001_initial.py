# Generated by Django 3.2.4 on 2021-08-07 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
