# Generated by Django 2.1.7 on 2019-04-15 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_category_instructorinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='contain_course',
        ),
    ]
