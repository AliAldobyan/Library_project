# Generated by Django 3.1.1 on 2020-09-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=120)),
                ('year_of_release', models.IntegerField()),
                ('isbn', models.IntegerField()),
                ('genre', models.CharField(max_length=120)),
                ('available', models.BooleanField()),
            ],
        ),
    ]
