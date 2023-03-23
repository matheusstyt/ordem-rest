# Generated by Django 4.1.7 on 2023-03-23 01:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(blank=True)),
                ('status', models.BooleanField(default=False)),
                ('fk_mestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('fk_de', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitacao_de_set', to=settings.AUTH_USER_MODEL)),
                ('fk_para', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitacao_para_set', to=settings.AUTH_USER_MODEL)),
                ('fk_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.session')),
            ],
        ),
        migrations.CreateModel(
            name='SessionPlayers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('fk_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fk_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.session')),
            ],
        ),
        migrations.CreateModel(
            name='SessionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_modificacao', models.DateTimeField()),
                ('descricao', models.CharField(blank=True, max_length=200)),
                ('fk_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.session')),
                ('origem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FriendList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_online', models.BooleanField(default=False)),
                ('fk_friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendlist_friend_set', to=settings.AUTH_USER_MODEL)),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendlist_user_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
