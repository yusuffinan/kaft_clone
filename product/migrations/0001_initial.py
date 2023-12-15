# Generated by Django 4.2.5 on 2023-12-13 17:34

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
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, default='', max_length=200, unique=True)),
                ('status', models.CharField(choices=[('draft', 'Taslak'), ('published', 'Yayinlandi'), ('delted', 'Silindi')], default='draft', max_length=10)),
                ('created_att', models.DateTimeField(auto_now_add=True)),
                ('uploated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, default='', max_length=200, unique=True)),
                ('status', models.CharField(choices=[('draft', 'Taslak'), ('published', 'Yayinlandi'), ('delted', 'Silindi')], default='draft', max_length=10)),
                ('content', models.TextField()),
                ('created_att', models.DateTimeField(auto_now_add=True)),
                ('uploated_at', models.DateTimeField(auto_now=True)),
                ('stock', models.PositiveSmallIntegerField(default=0)),
                ('price', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]