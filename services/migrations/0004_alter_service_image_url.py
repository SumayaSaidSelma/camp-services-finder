# Generated by Django 5.1.1 on 2024-09-29 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_remove_service_image_service_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]