# Generated by Django 4.1.7 on 2023-02-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_product_bookdate_remove_product_booking_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_booked',
            field=models.BooleanField(default=False),
        ),
    ]