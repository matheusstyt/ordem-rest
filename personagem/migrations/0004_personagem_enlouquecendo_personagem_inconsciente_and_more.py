# Generated by Django 4.1.7 on 2023-04-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("personagem", "0003_rename_peso_acessoriospersonagem_espaco_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="personagem",
            name="enlouquecendo",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="personagem",
            name="inconsciente",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="personagem",
            name="lesao_grave",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="personagem",
            name="morrendo",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="personagem",
            name="traumatizado",
            field=models.BooleanField(default=False),
        ),
    ]
