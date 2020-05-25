# Generated by Django 2.2.9 on 2020-02-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0003_auto_20200219_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='score_ext',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='groupe',
            name='equipe',
            field=models.ManyToManyField(through='presentation.Classement', to='presentation.Club'),
        ),
    ]