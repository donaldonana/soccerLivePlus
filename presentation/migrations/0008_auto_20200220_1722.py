# Generated by Django 2.2.9 on 2020-02-20 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0007_auto_20200220_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupe',
            name='equipe',
            field=models.ManyToManyField(through='presentation.Classement', to='presentation.Club'),
        ),
    ]
