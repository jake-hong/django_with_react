# Generated by Django 4.0 on 2021-12-23 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0005_alter_post_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
    ]