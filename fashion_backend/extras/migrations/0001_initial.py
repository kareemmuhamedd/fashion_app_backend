# Generated by Django 4.2.5 on 2024-09-18 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isVerified', models.BooleanField(default=False)),
                ('otp', models.CharField(default='', max_length=6)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('isDefault', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('addressType', models.CharField(choices=[('home', 'Home'), ('office', 'Office'), ('school', 'School')], default='home', max_length=10)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
