# Generated by Django 2.1.7 on 2019-04-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_component_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='CECU',
            field=models.IntegerField(default=6),
        ),
        migrations.AddField(
            model_name='courset',
            name='CECU',
            field=models.IntegerField(default=6),
        ),
    ]
