# Generated by Django 5.1.1 on 2024-09-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfile',
            name='name',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
