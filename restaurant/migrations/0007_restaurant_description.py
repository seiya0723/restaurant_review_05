# Generated by Django 3.2.11 on 2022-02-18 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_restaurant_judge_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='description',
            field=models.CharField(default='店舗説明文', max_length=2000, verbose_name='店舗紹介文'),
            preserve_default=False,
        ),
    ]
