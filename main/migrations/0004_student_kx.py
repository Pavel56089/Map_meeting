# Generated by Django 2.1.3 on 2019-02-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_student_koordinates'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='kx',
            field=models.BigIntegerField(default='55'),
        ),
    ]