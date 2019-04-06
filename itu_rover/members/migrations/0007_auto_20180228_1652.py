# Generated by Django 2.0.1 on 2018-02-28 13:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20180228_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='teamadvisor',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teamadvisor',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
