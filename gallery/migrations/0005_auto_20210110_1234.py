# Generated by Django 3.1.5 on 2021-01-10 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20210110_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]