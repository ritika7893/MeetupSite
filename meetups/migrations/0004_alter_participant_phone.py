# Generated by Django 5.0.2 on 2025-04-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0003_rename_participants_meetup_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
