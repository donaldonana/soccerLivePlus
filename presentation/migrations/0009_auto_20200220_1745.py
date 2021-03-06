# Generated by Django 2.2.9 on 2020-02-20 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0008_auto_20200220_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='stade',
        ),
        migrations.RemoveField(
            model_name='match',
            name='stade',
        ),
        migrations.AddField(
            model_name='stade',
            name='match',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='presentation.Match'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='groupe',
            name='equipe',
            field=models.ManyToManyField(through='presentation.Classement', to='presentation.Club'),
        ),
    ]
