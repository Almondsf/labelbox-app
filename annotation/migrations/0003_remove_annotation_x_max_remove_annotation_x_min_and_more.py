# Generated by Django 5.1.4 on 2024-12-18 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0002_remove_image_image_image_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='x_max',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='x_min',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='y_max',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='y_min',
        ),
        migrations.AddField(
            model_name='annotation',
            name='height',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='annotation',
            name='width',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='annotation',
            name='x',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='annotation',
            name='y',
            field=models.FloatField(null=True),
        ),
    ]
