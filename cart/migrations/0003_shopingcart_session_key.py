# Generated by Django 4.2.5 on 2023-12-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_shopingcart_total_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopingcart',
            name='session_key',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
