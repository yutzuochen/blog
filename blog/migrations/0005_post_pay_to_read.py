# Generated by Django 4.1.3 on 2022-11-12 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pay_to_read',
            field=models.FloatField(default=0),
        ),
    ]
