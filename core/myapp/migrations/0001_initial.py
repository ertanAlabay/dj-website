# Generated by Django 5.1 on 2024-08-13 10:24

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('date', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('writerName', models.CharField(max_length=100)),
                ('writerTitle', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='gallery/img')),
                ('file', models.FileField(upload_to='gallery/pdf')),
            ],
        ),
        migrations.CreateModel(
            name='NumberWorkPacket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='number_workpacket/img')),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='partners/img')),
                ('website', models.URLField(max_length=150)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='slides/img')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('URL', models.URLField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='slides/img')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='videos/img')),
                ('URL', models.URLField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='WorkPacket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='workpackets/img')),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='workpackets/pdf')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('numberpacket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.numberworkpacket')),
            ],
        ),
    ]