# Generated by Django 4.1.3 on 2022-11-12 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField(default=0)),
                ('user_id', models.FloatField()),
            ],
        ),
    ]
