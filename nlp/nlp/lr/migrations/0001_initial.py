# Generated by Django 2.2.11 on 2020-04-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='endpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default=' ', max_length=50)),
                ('lastName', models.CharField(default=' ', max_length=50)),
                ('income', models.IntegerField()),
                ('age', models.IntegerField()),
                ('rooms', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('population', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]