# Generated by Django 3.0.5 on 2023-12-07 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0040_auto_20231207_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='Select One', null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.Category'),
        ),
    ]
