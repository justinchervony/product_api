# Generated by Django 4.1.1 on 2022-09-20 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.CharField(default='no picture', max_length=255),
        ),
    ]