# Generated by Django 5.0.1 on 2024-01-14 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_background_img_img2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='gallery/')),
            ],
        ),
    ]