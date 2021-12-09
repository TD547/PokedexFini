# Generated by Django 3.2.7 on 2021-12-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0004_auto_20211207_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='team',
            name='name',
        ),
        migrations.AddField(
            model_name='team',
            name='pokemons',
            field=models.CharField(default=None, max_length=4096),
        ),
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
