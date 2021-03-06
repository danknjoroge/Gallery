# Generated by Django 4.0.3 on 2022-03-24 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_alter_image_options_remove_image_dep'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default=None, max_length=71, null=b'I01\n')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=b'I01\n', default=None, max_length=71)),
            ],
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(null=b'I01\n', on_delete=django.db.models.deletion.CASCADE, to='photos.category'),
            preserve_default=b'I01\n',
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(null=b'I01\n', on_delete=django.db.models.deletion.CASCADE, to='photos.location'),
            preserve_default=b'I01\n',
        ),
    ]
