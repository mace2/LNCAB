# Generated by Django 2.1.5 on 2019-03-12 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0016_auto_20190311_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='juego',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22')], default=55, max_length=2),
            preserve_default=False,
        ),
    ]
