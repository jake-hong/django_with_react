# Generated by Django 4.0 on 2021-12-23 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='insta/post/%Y/%m/%d'),
        ),
    ]
