# Generated by Django 2.1.7 on 2019-04-01 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_component_componenttype'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='modulet',
            name='counter',
            field=models.IntegerField(default='1'),
        ),
    ]
