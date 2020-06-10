# Generated by Django 3.0.6 on 2020-05-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('family', models.IntegerField()),
                ('contact', models.CharField(max_length=15)),
                ('arrival', models.CharField(max_length=30)),
                ('depart', models.CharField(max_length=30)),
                ('total', models.IntegerField()),
            ],
        ),
    ]
