# Generated by Django 5.0.7 on 2024-07-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='activity_photos/'),
        ),
    ]