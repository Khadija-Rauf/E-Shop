# Generated by Django 4.0.5 on 2022-06-13 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinestore', '0003_item_category_item_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=120)),
        ),
    ]