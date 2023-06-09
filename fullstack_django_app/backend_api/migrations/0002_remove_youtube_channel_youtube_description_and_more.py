# Generated by Django 4.2 on 2023-04-22 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtube',
            name='channel',
        ),
        migrations.AddField(
            model_name='youtube',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='youtube',
            name='link',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='youtube',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
