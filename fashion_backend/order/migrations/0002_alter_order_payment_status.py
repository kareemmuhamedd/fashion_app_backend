# Generated by Django 4.2.5 on 2024-09-26 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('paid', 'Paid'), ('failed', 'Failed'), ('cancelled', 'Cancelled')], max_length=255),
        ),
    ]
