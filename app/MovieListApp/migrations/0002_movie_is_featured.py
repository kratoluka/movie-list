# Generated by Django 4.1.2 on 2022-10-07 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieListApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_featured',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
