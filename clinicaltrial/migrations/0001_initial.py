# Generated by Django 2.0.2 on 2018-03-03 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrialMaster',
            fields=[
                ('trial_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('is_blacklisted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'ct_trial_master',
            },
        ),
        migrations.CreateModel(
            name='TrialStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Status')),
                ('trial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicaltrial.TrialMaster')),
            ],
            options={
                'db_table': 'ct_trial_status',
            },
        ),
    ]
