# Generated by Django 2.2.9 on 2020-02-19 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0005_auto_20200219_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='jr_joue',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='nbr_equipes',
        ),
        migrations.AddField(
            model_name='classement',
            name='competition',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='presentation.Competition'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='groupe',
            name='equipe',
            field=models.ManyToManyField(through='presentation.Classement', to='presentation.Club'),
        ),
    ]
