# Generated by Django 4.1.7 on 2023-03-04 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinokino', '0017_alter_episode_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='favorite',
            field=models.ManyToManyField(to='kinokino.userprofile'),
        ),
    ]
