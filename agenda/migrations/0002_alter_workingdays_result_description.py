# Generated by Django 5.1.3 on 2025-01-16 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workingdays',
            name='result_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
