# Generated by Django 5.0.6 on 2024-06-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0019_sitesetup_show_events_sitesetup_show_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetup',
            name='slide1_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='slide1_title',
            field=models.CharField(blank=True, max_length=65, null=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='slide2_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='slide2_title',
            field=models.CharField(blank=True, max_length=65, null=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='slide3_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='slide3_title',
            field=models.CharField(blank=True, max_length=65, null=True),
        ),
    ]