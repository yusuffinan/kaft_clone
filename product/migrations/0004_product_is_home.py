# Generated by Django 4.2.5 on 2023-12-16 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
    ]
