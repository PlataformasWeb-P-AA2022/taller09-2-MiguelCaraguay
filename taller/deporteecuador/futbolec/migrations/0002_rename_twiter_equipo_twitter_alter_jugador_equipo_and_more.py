# Generated by Django 4.0.5 on 2022-06-14 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('futbolec', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='twiter',
            new_name='twitter',
        ),
        migrations.AlterField(
            model_name='jugador',
            name='equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipo', to='futbolec.equipo'),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='sueldo',
            field=models.FloatField(verbose_name='sueldo'),
        ),
    ]
