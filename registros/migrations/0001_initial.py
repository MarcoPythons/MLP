# Generated by Django 3.1.1 on 2020-10-22 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('run', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=60)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'cliente',
                'ordering': ['run'],
            },
        ),
        migrations.CreateModel(
            name='cuenta',
            fields=[
                ('run', models.OneToOneField(max_length=10, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='registros.cliente')),
                ('password', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'cuenta',
                'ordering': ['run'],
            },
        ),
    ]