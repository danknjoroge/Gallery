# Generated by Django 4.0.3 on 2022-03-25 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=b'I00\n', upload_to='pics/'),
        ),
    ]
