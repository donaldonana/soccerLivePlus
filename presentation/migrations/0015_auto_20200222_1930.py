# Generated by Django 2.2.9 on 2020-02-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0014_auto_20200222_1927'),
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
            field=models.CharField(choices=[('EC', 'EN_COUR'), ('FT', 'FULL_TIME'), ('RPT', 'REPORTER')], default='A VENIR', max_length=2),
        ),
    ]
