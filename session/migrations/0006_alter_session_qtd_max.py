# Generated by Django 4.1.7 on 2023-03-26 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0005_alter_session_qtd_max'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='qtd_max',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]