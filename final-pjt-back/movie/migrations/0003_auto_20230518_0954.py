# Generated by Django 3.2.18 on 2023-05-18 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_genre_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='keyword_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_keyword',
            field=models.ManyToManyField(related_name='movie_keyword', to='movie.keyword'),
        ),
    ]
