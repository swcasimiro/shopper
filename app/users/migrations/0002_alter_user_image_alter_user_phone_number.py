# Generated by Django 5.0.1 on 2024-01-11 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default=True, null=True, upload_to='users_images', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, default='0', max_length=10, null=True),
        ),
    ]
