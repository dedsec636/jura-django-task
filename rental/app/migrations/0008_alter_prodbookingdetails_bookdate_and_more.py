# Generated by Django 4.1.7 on 2023-02-18 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_prodbookingdetails_bookdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodbookingdetails',
            name='bookdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='prodbookingdetails',
            name='booking_end',
            field=models.DateField(),
        ),
    ]
