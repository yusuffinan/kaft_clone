# Generated by Django 4.2.5 on 2023-12-15 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='gender',
            field=models.CharField(choices=[('man', 'Erkek'), ('woman', 'Kadin'), ('unisex', 'Unisex')], default='unisex', max_length=6),
        ),
    ]