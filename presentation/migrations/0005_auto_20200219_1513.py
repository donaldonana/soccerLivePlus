# Generated by Django 2.2.9 on 2020-02-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0004_auto_20200219_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupe',
            name='equipe',
            field=models.ManyToManyField(through='presentation.Classement', to='presentation.Club'),
        ),
    ]
