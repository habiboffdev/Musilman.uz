# Generated by Django 3.1.13 on 2021-09-04 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sura', '0002_ayah_audio_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sura',
            name='surah_ayahs_number',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='sura',
            name='surah_number',
            field=models.CharField(max_length=150),
        ),
    ]
