# Generated by Django 5.1.3 on 2024-12-01 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Fanlar',
            },
        ),
        migrations.CreateModel(
            name='Yonalish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('aktiv', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Yonalishlar',
            },
        ),
        migrations.CreateModel(
            name='Ustoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=50)),
                ('yosh', models.PositiveSmallIntegerField()),
                ('daraja', models.CharField(choices=[('Bakalavr', 'Bakalavr'), ('Magistr', 'Magistor'), ('Doktor', 'Doktor')], max_length=50)),
                ('fan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.fan')),
            ],
            options={
                'verbose_name_plural': 'Ustozlar',
            },
        ),
        migrations.AddField(
            model_name='fan',
            name='yonalish',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.yonalish'),
        ),
    ]