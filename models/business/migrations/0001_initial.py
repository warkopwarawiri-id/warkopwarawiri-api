# Generated by Django 3.2 on 2022-05-03 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, default=None, null=True)),
                ('name', models.CharField(max_length=100)),
                ('location_lat', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('location_lng', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.account')),
                ('picture', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='file.file')),
            ],
            options={
                'db_table': 'business',
                'managed': True,
            },
        ),
    ]