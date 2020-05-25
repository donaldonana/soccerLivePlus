# Generated by Django 2.2.9 on 2020-02-20 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0012_auto_20200220_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='pays_origine',
            field=models.CharField(choices=[('F', 'France'), ('A', 'Allemagne'), ('AG', 'Angleterre'), ('E', 'Espagne')], default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='groupe',
            name='equipe',
            field=models.ManyToManyField(through='presentation.Classement', to='presentation.Club'),
        ),
    ]
