# Generated by Django 2.1.5 on 2019-03-07 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cede', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='coach',
            name='end_date',
            field=models.DateTimeField(verbose_name='end date'),
        ),
        migrations.AddField(
            model_name='team',
            name='nombre_Coach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Coach'),
        ),
    ]
