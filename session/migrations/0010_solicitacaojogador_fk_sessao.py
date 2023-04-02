# Generated by Django 4.1.7 on 2023-03-31 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("session", "0009_solicitacaojogador_jogadoressessao"),
    ]

    operations = [
        migrations.AddField(
            model_name="solicitacaojogador",
            name="fk_sessao",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="solicitacao_jogador_sessao_set",
                to="session.session",
            ),
            preserve_default=False,
        ),
    ]