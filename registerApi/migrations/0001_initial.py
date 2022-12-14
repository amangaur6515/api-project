# Generated by Django 4.1.1 on 2022-12-11 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=200)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=100)),
                ('MobileNo', models.IntegerField()),
                ('Address', models.CharField(max_length=500)),
                ('Batch', models.CharField(max_length=200)),
                ('JoiningDate', models.DateField()),
            ],
        ),
    ]
