# Generated by Django 2.1.5 on 2019-03-11 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20190311_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='coach',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='teams.Coach'),
        ),
    ]
