# Generated by Django 3.2.18 on 2023-04-03 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0016_rename_fk_resistencias_resistencias_fk_resistencia'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArmamentoUser',
            new_name='Armamentos',
        ),
        migrations.RemoveField(
            model_name='armamento',
            name='fk_user',
        ),
        migrations.RemoveField(
            model_name='armamentos',
            name='fk_user',
        ),
        migrations.AddField(
            model_name='armamentos',
            name='fk_session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='session.session'),
            preserve_default=False,
        ),
    ]