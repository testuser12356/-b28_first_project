# Generated by Django 5.1.7 on 2025-03-24 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_news_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('order_num',)},
        ),
    ]
