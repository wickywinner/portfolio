# Generated by Django 3.0.6 on 2020-05-26 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.IntegerField()),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
    ]
