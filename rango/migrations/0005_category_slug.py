# Generated by Django 2.1.3 on 2018-12-02 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]