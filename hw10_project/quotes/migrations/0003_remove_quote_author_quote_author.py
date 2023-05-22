# Generated by Django 4.2 on 2023-04-29 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_alter_author_born_date_alter_author_fullname_quote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='author',
        ),
        migrations.AddField(
            model_name='quote',
            name='author',
            field=models.ManyToManyField(to='quotes.author'),
        ),
    ]
