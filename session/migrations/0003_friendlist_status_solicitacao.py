# Generated by Django 4.1.7 on 2023-03-27 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("session", "0002_session_descricao"),
    ]

    operations = [
        migrations.AddField(
            model_name="friendlist",
            name="status_solicitacao",
            field=models.BooleanField(default=False),
        ),
    ]
