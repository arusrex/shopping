# Generated by Django 5.0.6 on 2024-06-16 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0020_sitesetup_slide1_description_sitesetup_slide1_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetup',
            name='img_history',
            field=models.ImageField(blank=True, null=True, upload_to='assets/img_history/%Y/%m/%d'),
        ),
    ]