# Generated by Django 5.0.6 on 2024-06-20 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_remove_book_libary_book_library'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='library',
            field=models.ManyToManyField(to='books.library'),
        ),
    ]
