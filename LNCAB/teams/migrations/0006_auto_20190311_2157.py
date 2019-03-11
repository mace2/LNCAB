# Generated by Django 2.1.5 on 2019-03-11 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20190311_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='coach',
            new_name='coach_id',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='state',
            new_name='state_id',
        ),
        migrations.AddField(
            model_name='team',
            name='city',
            field=models.CharField(default='', max_length=50, verbose_name='city'),
        ),
    ]