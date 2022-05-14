# Generated by Django 4.0.3 on 2022-04-05 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artgallery', '0002_post_sociallink_alter_category_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='videoart',
            fields=[
                ('videoId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('artist', models.TextField()),
                ('videoLink', models.URLField()),
                ('socialLink', models.URLField()),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artgallery.category')),
            ],
        ),
    ]
