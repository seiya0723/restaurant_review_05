# Generated by Django 3.2.11 on 2022-02-04 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20220128_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(default='test.png', upload_to='restaurant/restaurant/image', verbose_name='店舗画像'),
            preserve_default=False,
        ),
    ]
