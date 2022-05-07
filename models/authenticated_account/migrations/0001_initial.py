# Generated by Django 3.2 on 2022-05-03 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthenticatedAccount',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('auth_token', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('fcm_token', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.account')),
            ],
            options={
                'db_table': 'authenticated_accounts',
                'managed': True,
            },
        ),
    ]
