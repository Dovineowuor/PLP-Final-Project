# Generated by Django 3.0.5 on 2023-12-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0021_auto_20231207_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
