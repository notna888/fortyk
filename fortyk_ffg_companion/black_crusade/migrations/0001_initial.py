# Generated by Django 3.0.11 on 2021-01-01 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialWeaponFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('ref', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('weapon_class', models.CharField(choices=[('B', 'Basic'), ('P', 'Pistol'), ('H', 'Heavy'), ('M', 'Melee')], max_length=1)),
                ('range', models.IntegerField()),
                ('rate_of_fire_single', models.BooleanField()),
                ('rate_of_fire_semi_auto', models.IntegerField()),
                ('rate_of_fire_full_auto', models.IntegerField()),
                ('damage', models.CharField(max_length=30)),
                ('damage_type', models.CharField(choices=[('E', 'Energy'), ('I', 'Impact'), ('R', 'Rending'), ('X', 'Explosive'), ('', 'Other')], max_length=1)),
                ('pen', models.IntegerField()),
                ('clip', models.IntegerField(null=True)),
                ('rld', models.CharField(max_length=10)),
                ('weight', models.IntegerField()),
                ('description', models.TextField()),
                ('las', models.BooleanField()),
                ('force', models.BooleanField()),
                ('ref', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='WeaponSpecial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_modifier', models.IntegerField(null=True)),
                ('special', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='black_crusade.SpecialWeaponFeature')),
                ('weapon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='black_crusade.Weapon')),
            ],
        ),
    ]
