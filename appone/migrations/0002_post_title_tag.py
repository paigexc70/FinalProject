# Generated by Django 4.1.3 on 2022-12-15 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Title', max_length=200),
        ),
    ]
