# Generated by Django 3.2.4 on 2021-07-29 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210729_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.TextField(),
        ),
    ]
