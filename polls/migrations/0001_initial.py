# Generated by Django 3.2.7 on 2021-09-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.IntegerField()),
                ('country', models.IntegerField()),
                ('street', models.TextField(max_length=200)),
            ],
        ),
    ]
