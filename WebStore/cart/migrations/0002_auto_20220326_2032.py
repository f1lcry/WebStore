# Generated by Django 3.2.7 on 2022-03-26 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_checked',
            field=models.BooleanField(default=True, verbose_name='is_cart_checked'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_quantity',
            field=models.IntegerField(default=0, verbose_name='Total quantity'),
        ),
    ]