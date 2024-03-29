# Generated by Django 4.0.5 on 2022-06-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinestore', '0019_coupon_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='being_delievered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='recieved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='refund_granted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='refund_requested',
            field=models.BooleanField(default=False),
        ),
    ]
