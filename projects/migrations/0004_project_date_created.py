# Generated by Django 3.2.4 on 2021-07-25 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_created',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
