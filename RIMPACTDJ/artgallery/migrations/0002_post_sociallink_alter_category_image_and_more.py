# Generated by Django 4.0.3 on 2022-04-04 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artgallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='socialLink',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='Media/artworks/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='Media/postartworks/'),
        ),
    ]
