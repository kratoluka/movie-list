# Generated by Django 4.1.2 on 2022-10-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieListApp', '0004_alter_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
