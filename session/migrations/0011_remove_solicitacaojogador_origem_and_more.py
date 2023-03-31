# Generated by Django 4.1.7 on 2023-03-31 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("session", "0010_solicitacaojogador_fk_sessao"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="solicitacaojogador",
            name="origem",
        ),
        migrations.AddField(
            model_name="solicitacaojogador",
            name="fk_mestre",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="solicitacao_jogador_fk_mestre_set",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="solicitacaojogador",
            name="fk_sessao",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="solicitacao_jogador_fk_sessao_set",
                to="session.session",
            ),
        ),
    ]
