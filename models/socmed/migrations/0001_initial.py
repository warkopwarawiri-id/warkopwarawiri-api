# Generated by Django 3.2 on 2022-05-03 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socmed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socmed_type', models.CharField(choices=[('IG', 'Instagram'), ('FB', 'Facebook'), ('TW', 'Twitter'), ('YT', 'Youtube'), ('TKT', 'Tiktok')], db_column='type', max_length=50)),
                ('owner_type', models.CharField(choices=[('USER', 'account'), ('BUSINESS', 'business')], max_length=100)),
                ('owner_ref', models.BigIntegerField(editable=False)),
                ('value', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=256)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'db_table': 'socmeds',
                'managed': True,
            },
        ),
    ]
