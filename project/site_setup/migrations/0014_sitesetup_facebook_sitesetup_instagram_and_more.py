# Generated by Django 5.0.6 on 2024-06-01 11:32

import utils.model_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0013_sitesetup_show_social_sitesetup_show_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetup',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='assets/logo/%Y/%m/%d/', validators=[utils.model_validators.validate_png]),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='show_logo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='x_twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='youtube',
            field=models.URLField(blank=True, null=True),
        ),
    ]