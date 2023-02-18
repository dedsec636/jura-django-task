# Generated by Django 4.1.7 on 2023-02-18 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('bookdate', models.TimeField(auto_now=True)),
                ('booking_end', models.TimeField()),
                ('product_booked', models.BooleanField()),
                ('product_cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.category')),
            ],
        ),
    ]
