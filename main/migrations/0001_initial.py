# Generated by Django 2.1.3 on 2019-02-24 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('group', models.IntegerField()),
                ('lyceum', models.CharField(max_length=20)),
                ('about', models.TextField()),
                ('transport', models.TextField()),
            ],
        ),
    ]
