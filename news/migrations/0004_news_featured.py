# Generated by Django 3.0.5 on 2021-01-14 07:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210114_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='featured',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
