# Generated by Django 4.2.8 on 2023-12-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files', verbose_name='File')),
                ('description', models.TextField(verbose_name='Description to file')),
                ('date', models.DateField(auto_now=True, verbose_name='Date added')),
            ],
            options={
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', verbose_name='Image')),
                ('description', models.TextField(verbose_name='Description to image')),
                ('date', models.DateField(auto_now=True, verbose_name='Date added')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('description', models.TextField(verbose_name='Description to text')),
                ('date', models.DateField(auto_now=True, verbose_name='Date added')),
            ],
            options={
                'verbose_name': 'text',
                'verbose_name_plural': 'texts',
            },
        ),
        migrations.CreateModel(
            name='URLs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=100000, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Description to URL')),
                ('date', models.DateField(auto_now=True, verbose_name='Date added')),
            ],
            options={
                'verbose_name': 'url',
                'verbose_name_plural': 'urls',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos', verbose_name='Video')),
                ('description', models.TextField(verbose_name='Description to video')),
                ('date', models.DateField(auto_now=True, verbose_name='Date added')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'videos',
            },
        ),
    ]
