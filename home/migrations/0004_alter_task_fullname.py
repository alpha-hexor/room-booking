# Generated by Django 4.0.3 on 2022-03-06 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_task_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='fullname',
            field=models.CharField(max_length=100),
        ),
    ]
