# Generated by Django 4.0.3 on 2022-03-23 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=b'I00\n', null=b'I00\n', upload_to='gallery/')),
            ],
        ),
    ]
