# Generated by Django 5.0.6 on 2024-06-28 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duong', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='street',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='street',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='street',
            name='importance_level',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='street',
            name='significance',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='street',
            name='stt',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
