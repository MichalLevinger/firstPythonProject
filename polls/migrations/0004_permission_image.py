# Generated by Django 3.2.7 on 2021-10-03 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_permission'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='image',
            field=models.ImageField(default='test', upload_to='images'),
            preserve_default=False,
        ),
    ]
