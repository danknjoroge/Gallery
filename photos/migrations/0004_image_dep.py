# Generated by Django 4.0.3 on 2022-03-23 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_image_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='dep',
            field=models.TextField(blank=b'I00\n'),
        ),
    ]
