# Generated by Django 5.1 on 2024-09-05 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_rename_people_modelview'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube', models.URLField(max_length=150)),
                ('facebook', models.URLField(max_length=150)),
                ('spotify', models.URLField(max_length=150)),
                ('instagram', models.URLField(max_length=150)),
            ],
        ),
    ]
