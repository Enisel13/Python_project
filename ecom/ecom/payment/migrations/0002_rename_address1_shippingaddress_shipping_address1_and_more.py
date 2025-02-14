# Generated by Django 5.1.4 on 2025-02-14 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address1',
            new_name='shipping_address1',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address2',
            new_name='shipping_address2',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='city',
            new_name='shipping_city',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='country',
            new_name='shipping_country',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='email',
            new_name='shipping_email',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='full_name',
            new_name='shipping_full_name',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='state',
            new_name='shipping_state',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='zipcode',
            new_name='shipping_zipcode',
        ),
    ]
