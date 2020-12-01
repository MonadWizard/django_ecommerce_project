# Generated by Django 3.1.2 on 2020-12-01 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201130_1107'),
        ('order', '0003_shopcart_variant'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.variants'),
        ),
    ]
