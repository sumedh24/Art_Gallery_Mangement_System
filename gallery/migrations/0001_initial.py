# Generated by Django 3.1.2 on 2020-10-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_id', models.IntegerField()),
                ('a_name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('style', models.CharField(max_length=30)),
            ],
        ),
    ]
