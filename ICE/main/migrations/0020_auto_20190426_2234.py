# Generated by Django 2.1.7 on 2019-04-26 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_quiz_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizt',
            name='numOfQuestion',
            field=models.IntegerField(default=0),
        ),
    ]