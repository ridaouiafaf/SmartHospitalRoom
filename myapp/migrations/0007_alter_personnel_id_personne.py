# Generated by Django 5.0.6 on 2024-06-07 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_id_personne_pointage_personnel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='id_personne',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]