# Generated by Django 5.0.1 on 2024-01-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_rename_about_about_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='logo',
            field=models.ImageField(default=1, upload_to='logo/'),
            preserve_default=False,
        ),
    ]
