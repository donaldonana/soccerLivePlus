# Generated by Django 2.2.9 on 2020-02-22 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0016_auto_20200222_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupe',
            name='equipe',
            field=models.ManyToManyField(through='presentation.Classement', to='presentation.Club'),
        ),
        migrations.AlterField(
            model_name='match',
            name='statu',
            field=models.CharField(choices=[('EN', 'EN ATTENDE'), ('EC', 'EN_COUR'), ('FT', 'FULL_TIME'), ('RPT', 'REPORTER')], default='EN ATTENDE', max_length=2),
        ),
    ]