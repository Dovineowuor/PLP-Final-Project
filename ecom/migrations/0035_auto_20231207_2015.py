# Generated by Django 3.0.5 on 2023-12-07 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0034_auto_20231207_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecom.Category'),
            preserve_default=False,
        ),
    ]
