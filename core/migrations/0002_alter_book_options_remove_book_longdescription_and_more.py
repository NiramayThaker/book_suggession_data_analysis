# Generated by Django 4.0.3 on 2023-09-28 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={},
        ),
        migrations.RemoveField(
            model_name='book',
            name='longDescription',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publishedDate',
        ),
        migrations.RemoveField(
            model_name='book',
            name='shortDescription',
        ),
    ]
