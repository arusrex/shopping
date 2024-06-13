# Generated by Django 5.0.6 on 2024-06-13 22:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_imagespost_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile/%Y/%m/%d')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='image', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Image',
                'verbose_name_plural': 'User Images',
            },
        ),
    ]
