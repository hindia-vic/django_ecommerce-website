# Generated by Django 4.0.4 on 2024-01-31 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_remove_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='on_sale',
            field=models.IntegerField(default=False),
        ),
    ]