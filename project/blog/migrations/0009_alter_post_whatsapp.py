# Generated by Django 5.0.6 on 2024-06-03 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_whatsapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='whatsapp',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
