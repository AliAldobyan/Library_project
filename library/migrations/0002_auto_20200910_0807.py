# Generated by Django 3.1.1 on 2020-09-10 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrowed',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='year_of_release',
            field=models.DateField(),
        ),
    ]
